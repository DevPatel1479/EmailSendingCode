import 'package:flutter/material.dart';

void main() {
  runApp(OtpE());
}

class OtpE extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'OTP Verification',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.green,
        hintColor: Color.fromARGB(255, 163, 247, 19), // Customize accent color
        fontFamily: 'Roboto', // Customize font family
      ),
      home: PhoneNumberScreen(),
    );
  }
}

class PhoneNumberScreen extends StatefulWidget {
  @override
  _PhoneNumberScreenState createState() => _PhoneNumberScreenState();
}

class _PhoneNumberScreenState extends State<PhoneNumberScreen> {
  TextEditingController _phoneNumberController = TextEditingController();
  final _formKey = GlobalKey<FormState>();

  String? _validatePhoneNumber(String? value) {
    if (value == null || value.isEmpty) {
      return 'Please enter your phone number';
    }
    if (value.length > 10 || !isNumeric(value)) {
      return 'Phone number must be exactly 10 digits';
    }
    return null;
  }

  bool isNumeric(String s) {
    if (s == null) {
      return false;
    }
    return double.tryParse(s) != null;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('OTP Verification'),
      ),
      body: Container(
        color:
            Color.fromARGB(255, 14, 182, 248), // Set background color to blue
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(
                'Enter your details for OTP verification:',
                style: TextStyle(
                    fontSize: 18,
                    color: Colors.white), // Set text color to white
              ),
              SizedBox(height: 20),
              TextFormField(
                controller: _phoneNumberController,
                keyboardType: TextInputType.phone,
                maxLength: 10, // Set maximum length of input to 10
                decoration: InputDecoration(
                  labelText: 'Phone Number',
                  counterText: '', // Remove the character count display
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.phone),
                ),
                validator: _validatePhoneNumber,
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState != null &&
                      _formKey.currentState!.validate()) {
                    // Perform OTP verification logic here
                    // This is where you can navigate to the OTP screen or handle the verification
                    String phoneNumber = _phoneNumberController.text;
                    print('Phone Number: $phoneNumber');
                  }
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color.fromARGB(255, 236, 238,
                      240), // Set button background color to blue
                  padding: EdgeInsets.symmetric(vertical: 15),
                ),
                child: Text(
                  'Get OTP',
                  style: TextStyle(fontSize: 18),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
