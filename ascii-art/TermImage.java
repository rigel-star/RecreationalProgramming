import java.io.*;
import java.awt.image.*;
import java.awt.Color;
import javax.imageio.ImageIO;

public class TermImage {
    public static void main(String[] args) {
        try {
            BufferedImage image = ImageIO.read(new File("./worker.jpeg"));
            final int H = image.getHeight();
            final int W = image.getWidth();
            for(int y = 0; y < H; y++) {
                for(int x = 0; x < W; x++) {
                    int rgb = image.getRGB(x, y);
                    Color color = new Color(rgb);
                    float r = color.getRed() * 0.2126f;
                    float g = color.getGreen() * 0.7152f;
                    float b = color.getBlue() * 0.0722f;
                    int gray = (int) r + (int) g + (int) b;
                    System.out.print(getAsciiChar((int) gray));
                }
                System.out.println();
            }
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }

    private static char getAsciiChar(int gray) {
        char[] asciiChars = {' ', '.', ':', '-', '=', '+', '*', '#', '%', '8', '@'};
        int index = gray * (asciiChars.length - 1) / 255;
        return asciiChars[index];
    }
}
