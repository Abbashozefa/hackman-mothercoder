import 'package:drowsy/view/login_screen.dart';
import 'package:flutter/material.dart';

class SwipingScreens extends StatefulWidget {
  @override
  _SwipingScreensState createState() => _SwipingScreensState();
}

class _SwipingScreensState extends State<SwipingScreens> {
  final PageController _pageController = PageController();
  int _currentPage = 0;
  final List<Map<String, dynamic>> _screens = [
    {
      'backgroundColor': Colors.blue,
      'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZOMEdJWeeehhmja6e5jK8aDiH_4mIiOc18g&usqp=CAU',
      'text': 'Do not drive sleepyhead, but if you do better call wakey-wakey',
    },
    {
      'backgroundColor': Colors.blue,
      'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZOMEdJWeeehhmja6e5jK8aDiH_4mIiOc18g&usqp=CAU',
      'text': 'When both of your eyes are completely closed for a given amount of time, you will be alerted',
    },
    {
      'backgroundColor': Colors.blue,
      'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZOMEdJWeeehhmja6e5jK8aDiH_4mIiOc18g&usqp=CAU',
      'text': 'When you yawn for a given amount of time, you will also be alerted',
    },
    {
      'backgroundColor': Colors.blue,
      'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZOMEdJWeeehhmja6e5jK8aDiH_4mIiOc18g&usqp=CAU',
      'text': 'wakey-wakey ensures that you drive safe',
    },
  ];

  void _nextPage() {
    if (_currentPage < _screens.length - 1) {
      _pageController.nextPage(
        duration: Duration(milliseconds: 300),
        curve: Curves.easeInOut,
      );

    }
    else{
      Navigator.push(context, MaterialPageRoute(builder: (context)=>LoginScreen1()));
    }
  }

  void _skipScreens() {
    Navigator.push(context, MaterialPageRoute(builder: (context)=>LoginScreen1()));
    // Implement your own logic here to navigate to a different page
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView.builder(
        controller: _pageController,
        itemCount: _screens.length,
        onPageChanged: (int page) {
          setState(() {
            _currentPage = page;
          });
        },
        itemBuilder: (BuildContext context, int index) {
          return SwipingScreen(
            backgroundColor: _screens[index]['backgroundColor'],
            image: _screens[index]['image'],
            text: _screens[index]['text'],
            onSkip: _skipScreens,
            onNext: _nextPage,

          );
        },
      ),
    );
  }
}

class SwipingScreen extends StatelessWidget {
  final Color backgroundColor;
  final String image;
  final String text;
  final VoidCallback onSkip;
  final VoidCallback onNext;

  SwipingScreen({
    required this.backgroundColor,
    required this.image,
    required this.text,
    required this.onSkip,
    required this.onNext,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      color: backgroundColor,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ClipRRect(
            borderRadius: BorderRadius.circular(80),
            child: Image.network(
              image,
              width: 200,
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20),
            child: Text(
              text,
              style: TextStyle(
                color: Colors.white,
                fontSize: 24,

                fontFamily: 'Pacifico',

              ),
              textAlign: TextAlign.center,
            ),
          ),
          SizedBox(height: 30),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextButton(
                onPressed: onSkip,
                child: Text(
                  'Skip',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 18,
                  ),
                ),
              ),
              SizedBox(width: 20),
              ElevatedButton(
                onPressed: onNext,
                style: ElevatedButton.styleFrom(
                  primary: Colors.white,
                ),
                child: Text(
                  'Next',
                  style: TextStyle(
                    color: Colors.blue,
                    fontSize: 18,
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
