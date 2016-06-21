package com.app.bonnie.bliss_countdown;


import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ImageButton;


public class YoutubeSongs extends AppCompatActivity {

    public android.widget.ImageButton CH_button, Olaf_button, DNCE_button;
    public void init() {
        CH_button = (ImageButton) findViewById(R.id.CH);
        Olaf_button = (ImageButton) findViewById(R.id.olaf);
        DNCE_button = (ImageButton) findViewById(R.id.DNCE);

        // set Calvin Harris Song
        CH_button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                Uri uri = Uri.parse("https://www.youtube.com/watch?v=ebXbLfLACGM");
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);
            }
        });

        // set Olaf Song
        Olaf_button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                Uri uri = Uri.parse("https://www.youtube.com/watch?v=UFatVn1hP3o");
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);

            }
        });

        // set DNCE Song
        DNCE_button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                Uri uri = Uri.parse("https://www.youtube.com/watch?v=vWaRiD5ym74");
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);

            }
        });


    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.youtube_songs);
        init();


    }
}