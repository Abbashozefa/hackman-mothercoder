import 'package:drowsy/view/google_map.dart';
import 'package:drowsy/view/help.dart';
import 'package:drowsy/view/statistics.dart';
import 'package:flutter/material.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:drowsy/view/signup_screen.dart';
import 'package:http/http.dart' as http;
import 'package:lottie/lottie.dart';
import 'package:animated_snack_bar/animated_snack_bar.dart';

class HomeScreen extends StatefulWidget {
  final String data;
  const HomeScreen({Key? key,required this.data}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  DatabaseReference? childRef;
  String displayedText = 'Default Text';
  String truee='hello';
  String name='';
  String anime ='';


  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    name=widget.data;
    childRef = FirebaseDatabase.instance.reference().child('contact').child(name);

    // Listen for value changes in the child
    childRef!.onValue.listen((event) {
      // Retrieve the updated key-value pair

      dynamic value = event.snapshot.value;
      Map<dynamic, dynamic> updatedData = value as Map<dynamic, dynamic>;

      // Assuming 'updatedKey' is the key you want to display
      if (updatedData.containsKey('alert')) {
        dynamic updatedValue = updatedData['alert'];

        // Update the displayed text
        setState(() {
          displayedText = updatedValue.toString();
          if(displayedText=='true'){
            anime='assets/animations/124134-yawing-laddu.json';
            truee='Hey! your loved one is feeling drowsiness while driving';
            AnimatedSnackBar.rectangle(
              'ALERT!',
              'Drowsiness detected',
              type: AnimatedSnackBarType.success,
              brightness: Brightness.dark,
            ).show(context);
          }else{
            anime = 'assets/animations/124251-neutral.json';
            truee='Such a lovely day it is';
          }
        });
      }

    });
  }

  Widget build(BuildContext context) {


    return Scaffold(
      backgroundColor: Colors.blue,
      body:Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Expanded(
            child: Center(
              child: Text(
               'Alert : '+displayedText,
                style: TextStyle(fontSize: 30.0,color: Colors.white,fontFamily: 'Indie',fontWeight: FontWeight.bold),
              ),
            ),
          ),
          Lottie.asset(
            anime,
            width: 200,
            height: 200,
            fit: BoxFit.contain,
          ),
          Expanded(
            child: Center(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Text(
                  truee,
                  style: TextStyle(fontSize: 20.0,color: Colors.white,fontFamily: 'Indie',fontWeight: FontWeight.bold),
                  textAlign: TextAlign.center,
                ),
              ),
            ),
          ),

          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              CardButton(
                icon: Icons.data_thresholding,
                label: 'Statistics',
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context)=>Statistics(username: widget.data,)));
                },
              ),
              CardButton(
                icon: Icons.location_on,
                label: 'Location',
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context)=>MapScreen(latitude: 12.972442, longitude: 77.580643)));
                },
              ),
            ],
          ),
        ],
      ),


    );
  }
}
class CardButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onPressed;

  const CardButton({
    Key? key,
    required this.icon,
    required this.label,
    required this.onPressed,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(

      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Container(
          height: 200,
          child: Card(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(20),
                side: BorderSide(color: Colors.grey, width: 1)
            ),
            elevation: 10.0,

            child: InkWell(
              onTap: onPressed,
              child: Padding(
                padding: const EdgeInsets.all(40.0),
                child: Column(
                  children: [
                    Icon(icon,color: Colors.blue,size: 40,),
                    SizedBox(height: 6.0),
                    Text(label,),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

}

