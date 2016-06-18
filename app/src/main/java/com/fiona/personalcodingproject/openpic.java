package com.fiona.personalcodingproject;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class OpenPic extends Activity {

    Button button;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.starting);
        addListenerOnButton();
    }

    public void addListenerOnButton() {
        final Context context = this;
        button = (Button)findViewById(R.id.imagebutton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(context, pic.class);
                    startActivity(intent);
            }
        });
    }
}
