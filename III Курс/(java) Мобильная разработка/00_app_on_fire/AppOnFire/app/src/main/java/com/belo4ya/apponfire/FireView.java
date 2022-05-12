package com.belo4ya.apponfire;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

import androidx.annotation.Nullable;

import java.util.Arrays;
import java.util.Random;

public class FireView extends View {
    private final Paint paint = new Paint();
    private final Random random = new Random();

    private static final int[] firePalette = {
            0xff070707,
            0xff1F0707,
            0xff2F0F07,
            0xff470F07,
            0xff571707,
            0xff671F07,
            0xff771F07,
            0xff8F2707,
            0xff9F2F07,
            0xffAF3F07,
            0xffBF4707,
            0xffC74707,
            0xffDF4F07,
            0xffDF5707,
            0xffDF5707,
            0xffD75F07,
            0xffD75F07,
            0xffD7670F,
            0xffCF6F0F,
            0xffCF770F,
            0xffCF7F0F,
            0xffCF8717,
            0xffC78717,
            0xffC78F17,
            0xffC7971F,
            0xffBF9F1F,
            0xffBF9F1F,
            0xffBFA727,
            0xffBFA727,
            0xffBFAF2F,
            0xffB7AF2F,
            0xffB7B72F,
            0xffB7B737,
            0xffCFCF6F,
            0xffDFDF9F,
            0xffEFEFC7,
            0xffFFFFFF
    };
    private int[] firePixels;
    private int fireWidth;
    private int fireHeight;
    private int[] bitmapPixels;
    private Bitmap bitmap;

    public FireView(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    protected void onSizeChanged(int w, int h, int oldw, int oldh) {
        fireWidth = 120;
        fireHeight = (int) (fireWidth / ((float) w / h));

        int size = fireWidth * fireHeight;

        firePixels = new int[size];
        Arrays.fill(firePixels, size - fireWidth, size, firePalette.length - 1);

        bitmap = Bitmap.createBitmap(fireWidth, fireHeight, Bitmap.Config.RGB_565);
        bitmapPixels = new int[size];
    }

    @Override
    protected void onDraw(Canvas canvas) {
        spreadFire();
        drawFire(canvas);
        invalidate();
    }

    private void spreadFire() {
        for (int y = 0; y < fireHeight - 1; y++) {
            for (int x = 0; x < fireWidth; x++) {
                int dx = random.nextInt(3) - 1;
                int dy = random.nextInt(4);
                int dt = random.nextInt(2);

                int newX = Math.min(Math.max(x + dx, 0), fireWidth - 1);
                int newY = Math.min(y + dy, fireHeight - 1);

                firePixels[x + fireWidth * y] = Math.max(firePixels[newX + fireWidth * newY] - dt, 0);
            }
        }
    }

    private void drawFire(Canvas canvas) {
        for (int y = 0; y < fireHeight; y++) {
            for (int x = 0; x < fireWidth; x++) {
                bitmapPixels[x + fireWidth * y] = firePalette[firePixels[x + fireWidth * y]];
            }
        }
        float scale = (float) getWidth() / fireWidth;
        canvas.scale(scale, scale);
        bitmap.setPixels(bitmapPixels, 0, fireWidth, 0, 0, fireWidth, fireHeight);
        canvas.drawBitmap(bitmap, 0, 0, paint);
    }
}
