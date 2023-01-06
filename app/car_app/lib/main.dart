import 'package:car_app/blocs/socket_state.dart';
import 'package:car_app/utils/car_socket.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_joystick/flutter_joystick.dart';

final socketBloc = SocketBloc();
final carSocket = CarSocket(addressValue: '0.0.0.0', status: 'Not Connected');

void main() {
  carSocket.main();
  socketBloc.add(IpAdressInfo(ipAdress: "No IP-adress"));
  socketBloc.add(ConnectionInfo(status: "Not connected"));

  runApp(const JoystickPage());
}

class JoystickPage extends StatelessWidget {
  const JoystickPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.black38,
        ),
        body: const JoystickWidget(),
      ),
    );
  }
}

class JoystickWidget extends StatefulWidget {
  const JoystickWidget({Key? key}) : super(key: key);

  @override
  _JoystickWidgetState createState() => _JoystickWidgetState();
}

class _JoystickWidgetState extends State<JoystickWidget> {
  final JoystickMode _joystickMode = JoystickMode.all;
  final myController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: SingleChildScrollView(
        child: GestureDetector(
          onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
          child: Column(children: [
            Wrap(
              alignment: WrapAlignment.center,
              runSpacing: 100,
              children: [
                Column(
                  children: [
                    Padding(
                      padding: const EdgeInsets.only(top: 50),
                      child: Text(
                        socketBloc.state.connectionState!,
                        style:
                            const TextStyle(color: Colors.white, fontSize: 40),
                      ),
                    ),
                    Text(socketBloc.state.ipAddress!,
                        style:
                            const TextStyle(color: Colors.white, fontSize: 20)),
                  ],
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    SizedBox(
                      width: 300,
                      child: TextField(
                        controller: myController,
                        textAlign: TextAlign.center,
                        autofocus: true,
                        cursorColor: Colors.white,
                        style: const TextStyle(color: Colors.white),
                        decoration: const InputDecoration(
                          enabledBorder: OutlineInputBorder(
                            borderSide:
                                BorderSide(color: Colors.grey, width: 0.0),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderSide:
                                BorderSide(color: Colors.grey, width: 0.0),
                          ),
                          border: UnderlineInputBorder(),
                          labelText: 'Enter the IP-address of the rasperry pi',
                          labelStyle:
                              TextStyle(color: Colors.white, fontSize: 14),
                          floatingLabelAlignment: FloatingLabelAlignment.center,
                        ),
                        inputFormatters: <TextInputFormatter>[
                          FilteringTextInputFormatter.allow(RegExp("[0-9.]")),
                          LengthLimitingTextInputFormatter(15)
                        ],
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.only(left: 10),
                      child: ElevatedButton(
                        child: const Text('Connect'),
                        onPressed: () {
                          setState(() {
                            socketBloc.add(ConnectionInfo(status: "Connected"));
                            socketBloc
                                .add(IpAdressInfo(ipAdress: myController.text));
                            carSocket.addressValue = myController.text;
                          });
                        },
                      ),
                    ),
                  ],
                ),
                Joystick(
                  onStickDragEnd: () {
                    carSocket.sendMessage("a|0|0");
                  },
                  mode: _joystickMode,
                  listener: (details) {
                    setState(() {
                      final x = details.x.toStringAsFixed(2);
                      final y = details.y.toStringAsFixed(2);
                      carSocket.sendMessage("a|$x|$y");
                    });
                  },
                ),
              ],
            )
          ]),
        ),
      ),
    );
  }
}
