import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:injectable/injectable.dart';

class SocketState {
  String? connectionState;
  String? ipAddress;

  SocketState();

  SocketState.copy(SocketState state)
      : connectionState = state.connectionState,
        ipAddress = state.ipAddress;
}

class SocketEvent {}

class LoadEvent extends SocketEvent {}

class ConnectionInfo extends SocketEvent {
  String status;
  ConnectionInfo({required this.status});
}

class IpAdressInfo extends SocketEvent {
  String ipAdress;
  IpAdressInfo({required this.ipAdress});
}

@injectable
class SocketBloc extends Bloc<SocketEvent, SocketState> {
  SocketBloc() : super(SocketState()) {
    on<LoadEvent>((event, emit) async {});
    init();

    on<ConnectionInfo>((event, emit) async {
      emit(
        SocketState.copy(state)..connectionState = event.status,
      );
    });

    on<IpAdressInfo>((event, emit) async {
      emit(
        SocketState.copy(state)..ipAddress = event.ipAdress,
      );
    });
  }

  void init() {
    add(LoadEvent());
  }
}
