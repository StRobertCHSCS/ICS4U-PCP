package com.app.bonnie.bliss_countdown;

// import useful android items
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

@SuppressWarnings("ConstantConditions")
public class MainActivity extends AppCompatActivity {

    // reference variables from elsewhere in the program
    private TextView show_days, show_hours, show_minutes, show_seconds;
    private TextView event_here;
    private Handler handler;
    protected Runnable runnable;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // set needed variables for later use
        show_days = (TextView) findViewById(R.id.show_days);
        show_hours = (TextView) findViewById(R.id.show_hours);
        show_minutes = (TextView) findViewById(R.id.show_minutes);
        show_seconds = (TextView) findViewById(R.id.show_seconds);
        event_here = (TextView) findViewById(R.id.event_here);

        //call countdown
        countDownStart();
    }

    public void countDownStart() {

        // create an instance of Handler and Runnable
        handler = new Handler();
        runnable = new Runnable() {
            @Override
            public void run() {
                // keep running method/countdown
                handler.postDelayed(this, 1000);
                try {
                    // create new instance of a simple date
                    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.CANADA);

                    // set date summer starts
                    Date futureDate = dateFormat.parse("2016-06-30");

                    // get current date
                    Date currentDate = new Date();

                    // calculate the number of days, hours, minutes, seconds until summer
                    if (!currentDate.after(futureDate)) {
                        long diff = futureDate.getTime() - currentDate.getTime();

                        //convert the difference in dates to days
                        long days = diff / (24 * 60 * 60 * 1000);
                        diff -= days * (24 * 60 * 60 * 1000);

                        //convert the difference in dates to hours
                        long hours = diff / (60 * 60 * 1000);
                        diff -= hours * (60 * 60 * 1000);

                        //convert the difference in dates to minutes
                        long minutes = diff / (60 * 1000);
                        diff -= minutes * (60 * 1000);

                        //convert the difference in dates to seconds
                        long seconds = diff / 1000;

                        // display the days, hours, minutes, seconds on screen
                        show_days.setText(String.valueOf(days));
                        show_hours.setText(String.valueOf(hours));
                        show_minutes.setText(String.valueOf(minutes));
                        show_seconds.setText(String.valueOf(seconds));

                    } else {

                        // if summer is already here (June 30th has passed) display that on screen
                        event_here.setVisibility(View.VISIBLE);
                        event_here.setText(R.string.yourevent);
                        textViewGone();
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        };
        handler.postDelayed(runnable, 1000);
    }
    public void textViewGone() {
        // if summer is here, do not show the boxes meant to display days, hours, minutes, seconds
        findViewById(R.id.LinearLayout10).setVisibility(View.GONE);
        findViewById(R.id.LinearLayout11).setVisibility(View.GONE);
        findViewById(R.id.LinearLayout12).setVisibility(View.GONE);
        findViewById(R.id.LinearLayout13).setVisibility(View.GONE);
        findViewById(R.id.event_here).setVisibility(View.GONE);
    }
}