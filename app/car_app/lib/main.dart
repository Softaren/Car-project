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

  runApp(const JoystickExampleApp());
}

class JoystickExampleApp extends StatelessWidget {
  const JoystickExampleApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Car app'),
          backgroundColor: Colors.black38,
        ),
        body: const JoystickExample(),
      ),
    );
  }
}

class JoystickExample extends StatefulWidget {
  const JoystickExample({Key? key}) : super(key: key);

  @override
  _JoystickExampleState createState() => _JoystickExampleState();
}

class _JoystickExampleState extends State<JoystickExample> {
  final JoystickMode _joystickMode = JoystickMode.all;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: SafeArea(
        child: Align(
          alignment: Alignment.center,
          child: Joystick(
            mode: _joystickMode,
            listener: (details) {
              setState(() {
                String x = details.x.toStringAsFixed(2);
                String y = details.y.toStringAsFixed(2);

                carSocket.sendMessage("a|$x|$y");
              });
            },
          ),
        ),
      ),
    );
  }
}

class JoystickModeDropdown extends StatelessWidget {
  final JoystickMode mode;
  final ValueChanged<JoystickMode> onChanged;

  const JoystickModeDropdown(
      {Key? key, required this.mode, required this.onChanged})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 150,
      child: Padding(
        padding: const EdgeInsets.only(left: 16.0),
        child: FittedBox(
          child: DropdownButton(
            value: mode,
            onChanged: (v) {
              onChanged(v as JoystickMode);
            },
            items: const [
              DropdownMenuItem(
                  child: Text('All Directions'), value: JoystickMode.all),
              DropdownMenuItem(
                  child: Text('Vertical And Horizontal'),
                  value: JoystickMode.horizontalAndVertical),
              DropdownMenuItem(
                  child: Text('Horizontal'), value: JoystickMode.horizontal),
              DropdownMenuItem(
                  child: Text('Vertical'), value: JoystickMode.vertical),
            ],
          ),
        ),
      ),
    );
  }
}
