package com.fiona.personalcodingproject;

import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;
import android.widget.MediaController;
import android.support.v7.app.AppCompatActivity;
import android.widget.VideoView;


public class main extends Activity {
    Button button;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_play_video);
    }
}
// Rapunzel video
public class main2 extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.laughing_fullscreen);

        VideoView videoView = (VideoView)findViewById(R.id.videoView);
        MediaController mediaController=new MediaController(this);
        mediaController.setAnchorView(videoView);
        Uri uri=Uri.parse("rtsp://r13---sn-vgqs7ner.googlevideo.com/Cj0LENy73wIaNAlIBfErgNgqRxMYDSANFC0Z82FXMOCoAUIASARgtdjU2NCE9btPigELRWxtS3N2ZHdDN00M/35338A718972CBCCF0C6F3E86A99F7CC7DB64B5C.50242B3E06D30B98C682E6F92F1A9C2018BB5A65/yt6/1/video.3gp");
        videoView.setMediaController(mediaController);
        videoView.setVideoURI(uri);
        videoView.requestFocus();
        videoView.start();
    }
}

