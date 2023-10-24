import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import javax.imageio.ImageIO;

import java.awt.image.BufferedImage;

public class Main {
    public static void main(String[] args) {
        try {
            InputStream in = new FileInputStream("./worker.jpeg");
            final int size = in.available();
            final int[][] output = new int[256][256];
            final int[] data = new int[size];
            int chr = 0;
            int idx = 0;
            while((chr = in.read()) != -1) {
                data[idx++] = chr;
            }

            for(int i = 0; i < size; i += 2) {
                int x = 0, y = 0;
                if((i + 1) < size) {
                    x = data[i];
                    y = data[i + 1];
                } else {
                    y = data[i];
                }
                if(output[x][y] < 255) {
                    output[x][y]++;
                }
            } 

            double max = 0;
            for(int x = 0; x < 256; x++) {
                for(int y = 0; y < 256; y++) {
                    double f = 0;
                    if(output[x][y] > 0) f = Math.log(output[x][y]);
                    if(f > max) max = f;
                }
            }

            BufferedImage outputImg = new BufferedImage(256, 256, BufferedImage.TYPE_INT_ARGB);
            for(int x = 0; x < 256; x++) {
                for(int y = 0; y < 256; y++) {
                    int rgb = (int) (Math.log(output[x][y]) / max) * 255;
                    int avg = 0xFF000000 | (rgb << 16) | (rgb << 8) | rgb;
                    outputImg.setRGB(x, y, avg);
                }
            }
            ImageIO.write(outputImg, "png", new File("./output.png"));
            in.close();
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
}