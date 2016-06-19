package com.fiona.personalcodingproject;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.view.View.OnClickListener;

public class LaughingActivity extends Activity {
    // reference to buttons
    Button button;

    @Override
    // store or save information to the button
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // connect to laughing_fullscreen XML file
        setContentView(R.layout.laughing_fullscreen);
        addListenerOnButton();
    }

    public void addListenerOnButton() {
        final Context context = this;
        // connect the button to the Rapunzel Image Button
        button = (ImageButton)findViewById(R.id.RapunzelButton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect main class to the LaughingActivity class (main class activated after LaughingActivity class)
            public void onClick(View v) {
                Intent intent = new Intent(context, main.class);
                    startActivity(intent);
            }
        });

    }
    public void addListenerOnButton() {
        final Context context = this;
        // connect the button to the LionKing Image Button
        button = (ImageButton) findViewById(R.id.LionKingButton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect main class to the LaughingActivity class (main class activated after LaughingActivity class)
            public void onClick(View v) {
                Intent intent = new Intent(context, main.class);
                startActivity(intent);
            }
        });
    }

    public void addListenerOnButton() {
        final Context context = this;
        // connect the button to the Elsa Image Button
        button = (ImageButton) findViewById(R.id.ElsaButton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect main class to the LaughingActivity class (main class activated after LaughingActivity class)
            public void onClick(View v) {
                Intent intent = new Intent(context, main.class);
                startActivity(intent);
            }
        });
    }

    public void addListenerOnButton() {
        final Context context = this;
        // connect the button to the Aladdin Image Button
        button = (ImageButton) findViewById(R.id.AladdinButton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect main class to the LaughingActivity class (main class activated after LaughingActivity class)
            public void onClick(View v) {
                Intent intent = new Intent(context, main.class);
                startActivity(intent);
            }
        });
    }

    public void addListenerOnButton() {
        final Context context = this;
        // connect the button to the Mulan Image Button
        button = (ImageButton) findViewById(R.id.MulanButton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect main class to the LaughingActivity class (main class activated after LaughingActivity class)
            public void onClick(View v) {
                Intent intent = new Intent(context, main.class);
                startActivity(intent);
            }
        });
    }

    public void addListenerOnButton() {
        final Context context = this;
        // connect the button to the Pocahontas Image Button
        button = (ImageButton) findViewById(R.id.PocahontasButton);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            // connect main class to the LaughingActivity class (main class activated after LaughingActivity class)
            public void onClick(View v) {
                Intent intent = new Intent(context, main.class);
                startActivity(intent);
            }
        });
    }
}