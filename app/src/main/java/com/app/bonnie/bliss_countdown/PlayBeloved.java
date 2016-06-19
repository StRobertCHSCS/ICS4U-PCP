package com.app.bonnie.bliss_countdown;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

public class PlayBeloved extends AppCompatActivity {

    MediaPlayer mySound;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.nature_screen);
        mySound = MediaPlayer.create(this,R.raw.beloved);
    }

    public void playNature(View view) {
        mySound.start();
    }

    public void pauseNature(View view) {
        mySound.pause();
    }

    public void stopNature(View view) {
        mySound.stop();
    }
}
