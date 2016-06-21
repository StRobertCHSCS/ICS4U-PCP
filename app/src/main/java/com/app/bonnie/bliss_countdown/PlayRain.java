package com.app.bonnie.bliss_countdown;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;


public class PlayRain extends AppCompatActivity {

    MediaPlayer mySound;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.rain_screen);
        mySound = MediaPlayer.create(this,R.raw.kiss_rain);
    }

    public void playRain(View view) {
        mySound.start();
    }

    public void pauseRain(View view) {
        mySound.pause();
    }

    public void stopRain(View view) {
        mySound.stop();
    }
}
