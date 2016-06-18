package com.fiona.personalcodingproject;

import android.os.Bundle;
import android.widget.Button;


public class pic extends OpenPic {
    // reference to button
    Button button;

    @Override
    // save information to the activity of the selected button
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //connect to image XML file
        setContentView(R.layout.image);
        // when press back, will go back to previous screen
        onBackPressed();
    }
}
