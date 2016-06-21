package com.app.bonnie.bliss_countdown;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

public class HomeScreen extends AppCompatActivity {

    public android.widget.Button countdown_button, youtube_button,soothing_songs;

    public void init() {
        countdown_button = (Button) findViewById(R.id.countdown_button);
        youtube_button = (Button) findViewById(R.id.youtube_button);
        soothing_songs = (Button) findViewById(R.id.soothing_songs);

        countdown_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent open_countdown = new Intent(HomeScreen.this, Countdown.class);
                startActivity(open_countdown);
            }
        });

        youtube_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent open_youtube = new Intent(HomeScreen.this, YoutubeSongs.class);
                startActivity(open_youtube);
            }
        });

        soothing_songs.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent open_piano = new Intent(HomeScreen.this, PlaySongs.class);
                startActivity(open_piano);
            }
        });
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.home_screen);
        init();
    }
}
