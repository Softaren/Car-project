import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_joystick/flutter_joystick.dart';

class CarSocket {
  String addressValue = "192.168.2.121";

  late RawDatagramSocket udpSocket;

  Future main() async {
    udpSocket = await RawDatagramSocket.bind(InternetAddress.anyIPv4, 65432);
    udpSocket.broadcastEnabled = true;
  }

  void sendMessage(String basicMessage) async {
    udpSocket.send(const Utf8Codec().encode(basicMessage),
        InternetAddress(addressValue), 65432);
  }
}

CarSocket carSocket = CarSocket();

void main() {
  carSocket.main();

  runApp(const JoystickPage());
}

class JoystickPage extends StatelessWidget {
  const JoystickPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Car app'),
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: SafeArea(
        child: Align(
          alignment: Alignment.center,
          child: Joystick(
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
        ),
      ),
    );
  }
}
