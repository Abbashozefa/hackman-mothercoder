import 'package:drowsy/view/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:drowsy/view/round_button.dart';

class VerifyScreen extends StatefulWidget {
  final String username;
  final String verificationId;
  const VerifyScreen({Key? key,required this.verificationId,required this.username}) : super(key: key);

  @override
  State<VerifyScreen> createState() => _VerifyScreenState();
}

class _VerifyScreenState extends State<VerifyScreen> {
  final verificationCodeController = TextEditingController();
  bool loading = false;
  final auth = FirebaseAuth.instance;


  @override
  void verify() async {
    final credential = PhoneAuthProvider.credential(
        verificationId: widget.verificationId,
        smsCode: verificationCodeController.text.toString());
    try {
      await auth.signInWithCredential(credential);
      Navigator.push(context, MaterialPageRoute(builder: (context) =>
          HomeScreen(data: widget.username )));
    } catch (e) {}
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Verify'),
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 30),
        child: Column(
          children: [
            SizedBox(
              height: 100,
            ),
            TextFormField(
              controller: verificationCodeController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(hintText: 'Enter 6 digit code'),
            ),
            SizedBox(
              height: 100,
            ),
            RoundButton(
                title: "Verify",
                loading: loading,
                ontap: () async {
                  setState(() {
                    loading = true;
                  });
                  final credential = PhoneAuthProvider.credential(
                      verificationId: widget.verificationId,
                      smsCode: verificationCodeController.text.toString());
                  try {
                    await auth.signInWithCredential(credential);
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => HomeScreen(data: verificationCodeController.text.toString())));
                  } catch (e) {
                    setState(() {
                      loading = false;
                    });
                  }
                })
          ],
        ),
      ),
    );
  }
}




