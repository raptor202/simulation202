<?php
//require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;



require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/SMTP.php';




if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$email = htmlspecialchars($_POST['email']);
        $password = htmlspecialchars($_POST['new_password']);


//    $to = 'hafiz.adnan@plantacorp.com';  // Replace with your email
        //$subject = 'New Contact Form Message';
        //  $body = "Name: $name\nEmail: $email";
        //$headers = "From: $email";
    

        $mail = new PHPMailer(true);

        try {
            //Server settings
            //$mail->SMTPDebug = SMTP::DEBUG_SERVER;                      //Enable verbose debug output
            $mail->isSMTP();                                            //Send using SMTP
            $mail->Host = 'smtp.gmail.com ';                     //Set the SMTP server to send through
            $mail->SMTPAuth = true;                                   //Enable SMTP authentication
            $mail->Username = 'muhammadalimanzer@gmail.com';                     //SMTP username
            $mail->Password = 'otmm iykl ejxj infn';                               //SMTP password
            $mail->SMTPSecure = 'TLS';            //Enable implicit TLS encryption
            $mail->Port = 587;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`

            //Recipients
            $mail->setFrom('muhammadalimanzer@gmail.com', 'Mailer');
            $mail->addAddress('it@plantacorp.com', 'IT');     //Add a recipient
             //Name is optional
            //$mail->addReplyTo('info@example.com', 'Information');
            //$mail->addCC('cc@example.com');
            //$mail->addBCC('bcc@example.com');

            //Attachments
            //$mail->addAttachment('/var/tmp/file.tar.gz');         //Add attachments
            //$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    //Optional name

            //Content
            $mail->isHTML(true);                                  //Set email format to HTML
            //$mail->Subject = 'Here is the subject';
            $mail->Body = 'HI <br>,  '.$email.   'clicked on the link with the following password'.$password. '<br> Just chill';
            //$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

            $mail->send();
            echo "Sent";
        } catch (Exception $e) {

            //echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
        }

}

