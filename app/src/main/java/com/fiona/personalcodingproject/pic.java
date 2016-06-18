package com.fiona.personalcodingproject;

import android.os.Bundle;
import android.widget.Button;


public class pic extends OpenPic {
    Button button;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.image);
        onBackPressed();
    }
}
