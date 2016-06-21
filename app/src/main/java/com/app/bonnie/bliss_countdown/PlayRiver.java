package com.app.bonnie.bliss_countdown;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;


public class PlayRiver extends AppCompatActivity{

    MediaPlayer mySound;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.river_screen);
        mySound = MediaPlayer.create(this,R.raw.river);
    }

    public void playMusic(View view) {
        mySound.start();
    }

    public void pauseMusic(View view) {
        mySound.pause();
    }

    public void stopMusic(View view) {
        mySound.stop();
    }
}
