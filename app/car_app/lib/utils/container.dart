import 'package:car_app/blocs/socket_state.dart';
import 'package:car_app/utils/car_socket.dart';
import 'package:get_it/get_it.dart';
import 'package:injectable/injectable.dart';

final getIt = GetIt.instance;

GetIt $initGetIt(
  GetIt gi, {
  String? environment,
  EnvironmentFilter? environmentFilter,
}) {
  final gh = GetItHelper(gi, environment, environmentFilter);
  gh.lazySingleton<SocketBloc>(() => SocketBloc());
  gh.lazySingleton<CarSocket>(
      () => CarSocket(addressValue: '0.0.0.0', status: 'Not Connected'));

  return gi;
}

@injectableInit
void configureInjection({String? environment}) =>
    $initGetIt(getIt, environment: environment);
