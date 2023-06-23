# BMI_Calculator

This program calculates the Body Mass Index (BMI) based on the weight and height entered by the user. It also provides a classification of the BMI result, indicating whether the person is underweight, normal weight, overweight, obese, severely obese, or morbidly obese.

## Usage

1. Run the program.
2. Enter your name when prompted.
3. Enter your weight in pounds.
4. Enter your height in inches.

The program will then calculate your BMI using the formula: BMI = (weight in pounds * 703) / (height in inches ** 2). It will display the calculated BMI value and provide a classification based on the following ranges:

- BMI <= 18.5: You are underweight.
- 18.5 < BMI <= 24.9: You are normal weight.
- 24.9 < BMI <= 29.9: You are overweight.
- 29.9 < BMI <= 34.9: You are obese.
- 34.9 < BMI <= 39.9: You are severely obese.
- BMI > 39.9: You are morbidly obese.

If the entered values for weight and height are invalid (i.e., non-numeric), the program will display an "Enter valid input" message.

## Dependencies

This program does not have any external dependencies. It runs on the standard Python library.

## License

This program is released under the [MIT License](LICENSE). You are free to use, modify, and distribute the code according to the terms and conditions of the license.

Please note that this BMI calculator is provided for informational purposes only and should not replace professional medical advice. Always consult with a healthcare professional for accurate assessment and guidance regarding your health and weight management.

Feel free to use and contribute to this open-source project. Suggestions, bug reports, and improvements are welcome.
