import java.applet.Applet;
import java.awt.*;
/*
    <applet code = "MyApplet" width = "300" height="200">
        <param name = "message" value = "Hello, Welcome to Java Applet!">
    </applet>
 */
public class MyApplet extends Applet {
    String message;
    public void init() {
        message = getParameter("message");
        if (message == null) {
            message = "Default message: Hello, Applet!";
        }
    }
    public void paint(Graphics g) {
        g.setFont(new Font("Arial", Font.BOLD, 14));
        g.drawString(message, 20, 100);
    }
}
// import javax.swing.*;
// import java.awt.*;

// class MySwingApp extends JFrame {
//     private String message;

//     public MySwingApp(String message) {
//         this.message = message;

//         // Set up the JFrame
//         setTitle("Applet");
//         setSize(400, 200);
//         setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//         setLocationRelativeTo(null);

//         JPanel panel = new JPanel() {
//             @Override
//             protected void paintComponent(Graphics g) {
//                 super.paintComponent(g);
//                 g.setFont(new Font("Arial", Font.BOLD, 16));
//                 g.drawString(message, 50, 100);
//             }
//         };
//         add(panel);
//     }

//     public static void main(String[] args) {
//         SwingUtilities.invokeLater(() -> {
//             MySwingApp app = new MySwingApp("Hello, Welcome to Java Applet!");
//             app.setVisible(true);
//         });
//     }
// }
