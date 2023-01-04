import 'dart:convert';
import 'dart:io';
import 'package:car_app/utils/container.dart';
import 'package:car_app/blocs/socket_state.dart';

class CarSocket {
  final socketBloc = getIt<SocketBloc>();
  String addressValue;
  String status;
  late RawDatagramSocket udpSocket;

  CarSocket({required this.addressValue, required this.status});

  Future main() async {
    udpSocket = await RawDatagramSocket.bind(InternetAddress.anyIPv4, 65432);
    udpSocket.broadcastEnabled = true;
  }

  void sendMessage(String basicMessage) async {
    udpSocket.send(const Utf8Codec().encode(basicMessage),
        InternetAddress(addressValue), 65432);
  }
}
