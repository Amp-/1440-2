void setup() {
  Serial.begin(115200);
}

void loop() {

 if ( Serial.available() )
  {
    char c = toupper(Serial.read());
    if ( c == 'A' )
  {
  while(true)
  {
    Serial.println("A_10V");
    delay(300);
  }
  }
    }
    else if ( c == 'B')
    {
      Serial.println("B_5A");
      delay(300);

    }

  }




  
}
