package com.app.bonnie.bliss_countdown;


import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ImageButton;

public class PlaySongs extends AppCompatActivity {

    public android.widget.ImageButton river_button, rain_button, nature_button;

    public void init() {
        river_button = (ImageButton) findViewById(R.id.river_button);
        rain_button = (ImageButton) findViewById(R.id.rain_button);
        nature_button = (ImageButton) findViewById(R.id.waves_button);

        river_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent open_flows = new Intent(PlaySongs.this, PlayRiver.class);
                startActivity(open_flows);
            }
        });

        rain_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent open_kiss = new Intent(PlaySongs.this, PlayRain.class);
                startActivity(open_kiss);
            }
        });

        nature_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent open_waves = new Intent(PlaySongs.this, PlayBeloved.class);
                startActivity(open_waves);
            }
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.play_songs);
        init();
    }
}
