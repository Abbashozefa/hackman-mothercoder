import 'package:animated_splash_screen/animated_splash_screen.dart';
import 'package:drowsy/main.dart';
import 'package:drowsy/view/landing_screen.dart';
import 'package:drowsy/view/login_screen.dart';
import 'package:flutter/material.dart';
class SplashScreen extends StatefulWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  Widget build(BuildContext context) {
    return AnimatedSplashScreen(

        splash: Icons.remove_red_eye_outlined,
        nextScreen: SwipingScreens(),
      duration: 2500,
      backgroundColor: Colors.white10,
      splashTransition: SplashTransition.fadeTransition,

    );
  }
}
