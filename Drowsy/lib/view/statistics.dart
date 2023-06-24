import 'package:flutter/material.dart';
import 'package:firebase_storage/firebase_storage.dart';

class Statistics extends StatefulWidget {
  final String username;
  const Statistics({Key? key,required this.username}):super(key: key);

  @override
  State<Statistics> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<Statistics> {

  late String imageUrl1;
  final storage = FirebaseStorage.instance;
  @override
  void initState() {
    super.initState();
    // Set the initial value of imageUrl to an empty string

    imageUrl1 = '';
    //Retrieve the imge grom Firebase Storage
    getImageUrl();
  }

  Future<void> getImageUrl() async {
    // Get the feference to the image file in Firebase Storage

    final ref1 = storage.ref().child(widget.username+'.png');
    // Get teh inageUrl to download URL

    final url1 = await ref1.getDownloadURL();
    setState(() {

      imageUrl1 = url1;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: const Text("Insights")),
      ),
      body: Column(
        children: [

          Center(
            child: Card(
              child: SizedBox(
                  height: 300,
                  child: Image(
                    image: NetworkImage(imageUrl1),
                    fit: BoxFit.cover,

                  )),
            ),
          )
        ],
      ),
    );
  }
}