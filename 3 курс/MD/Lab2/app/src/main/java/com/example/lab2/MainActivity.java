package com.example.lab2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class MainActivity extends AppCompatActivity {
    
    Button button1;
    Button button2;
    Button button3;
    Button button4;
    Button button5;
    Button button6;
    Button button7;
    Button button8;
    Button button9;
    Button button0;

    Button buttonAddition;
    Button buttonSubtraction;
    Button buttonMultiplication;
    Button buttonDivision;
    Button buttonResult;

    TextView textNumber1;
    TextView textOperation;
    TextView textNumber2;
    TextView textEquals;
    TextView textResult;

    Boolean isFirstNumber;
    Boolean isNewExpression;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        button1 = findViewById(R.id.button1);
        button2 = findViewById(R.id.button2);
        button3 = findViewById(R.id.button3);
        button4 = findViewById(R.id.button4);
        button5 = findViewById(R.id.button5);
        button6 = findViewById(R.id.button6);
        button7 = findViewById(R.id.button7);
        button8 = findViewById(R.id.button8);
        button9 = findViewById(R.id.button9);
        button0 = findViewById(R.id.button0);

        buttonAddition = findViewById(R.id.buttonAddition);
        buttonSubtraction = findViewById(R.id.buttonSubtraction);
        buttonMultiplication = findViewById(R.id.buttonMultiplication);
        buttonDivision = findViewById(R.id.buttonDivision);
        buttonResult = findViewById(R.id.buttonResult);

        textNumber1 = findViewById(R.id.textNumber1);
        textOperation = findViewById(R.id.textOperation);
        textNumber2 = findViewById(R.id.textNumber2);
        textResult = findViewById(R.id.textResult);

        isFirstNumber = true;
        isNewExpression = false;
        textEquals.setVisibility(View.INVISIBLE);

        button0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "0");
            }
        });

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "1");
            }
        });

        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "2");
            }
        });

        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "3");
            }
        });

        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "4");
            }
        });

        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "5");
            }
        });

        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "6");
            }
        });

        button7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "7");
            }
        });

        button8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "8");
            }
        });

        button9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                numberPicker(isFirstNumber, "9");
            }
        });


        buttonAddition.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                isFirstNumber = false;
                textOperation.setText("+");
            }
        });

        buttonSubtraction.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                isFirstNumber = false;
                textOperation.setText("-");
            }
        });

        buttonMultiplication.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                isFirstNumber = false;
                textOperation.setText("*");
            }
        });

        buttonDivision.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                isFirstNumber = false;
                textOperation.setText("/");
            }
        });

        buttonResult.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewExpression) {
                    resetExpression();
                }
                buttonResultClicked(textOperation.getText().toString());
            }
        });

    }

    private void numberPicker(Boolean isFirstNumber, String value) {
        if (isFirstNumber) {
            textNumber1.setText(textNumber1.getText() + value);
        } else {
            textNumber2.setText(textNumber2.getText() + value);
        }
    }
    
    private void buttonResultClicked(String Operation) {

        Double result = 0.0;
        Double firstValue = Double.parseDouble(textNumber1.getText().toString());
        Double secondValue = Double.parseDouble(textNumber2.getText().toString());

        textEquals.setVisibility(View.VISIBLE);
        switch (Operation) {
            case ("+"):
                result = firstValue + secondValue;
                break;
            case ("-"):
                result = firstValue - secondValue;
                break;
            case ("*"):
                result = firstValue * secondValue;
                break;
            case ("/"):
                result = firstValue / secondValue;
                break;
        }
        textResult.setText(Double.toString(round(result, 5)));
        isNewExpression = true;
    }


    private void resetExpression() {
        isFirstNumber = true;
        isNewExpression = false;
        textNumber1.setText("");
        textOperation.setText("");
        textNumber2.setText("");
        textEquals.setVisibility(View.INVISIBLE);
        textResult.setText("");

    }


    private double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = BigDecimal.valueOf(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}