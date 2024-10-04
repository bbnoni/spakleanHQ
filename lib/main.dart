import 'package:flutter/material.dart';

import 'screens/login_screen.dart';

void main() {
  runApp(SpakleanApp());
}

class SpakleanApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Spaklean App',
      theme: ThemeData(
        primarySwatch: Colors.lightBlue,
      ),
      home: LoginScreen(),
    );
  }
}
