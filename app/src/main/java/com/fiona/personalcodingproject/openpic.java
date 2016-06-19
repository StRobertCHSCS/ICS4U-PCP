package com.fiona.personalcodingproject;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class OpenPic extends Activity {
    // reference button
    Button button;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // connect to starting XML file
        setContentView(R.layout.starting);
        addListenerOnButton();
    }

    public void addListenerOnButton() {
        final Context context = this;
        // connect to imagebutton id from the starting XML file
        button = (Button)findViewById(R.id.imagebutton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect openpic class to the pic class (pic class activated after openpic class)
            public void onClick(View v) {
                Intent intent = new Intent(context, pic.class);
                    startActivity(intent);
            }
        });
    }
}
