#include <LedControl.h>

const byte NB_MAX7219 = 16;

const byte CS = 10;
const byte CLK = 11;
const byte DIN = 12;

LedControl lc = LedControl(DIN, CLK, CS, NB_MAX7219);

byte displayBuffer[8 * NB_MAX7219];

const byte alphabet[67][8] = {
  {B00000000, B00111000, B01000100, B01001100, B01010100, B01100100, B01000100, B00111000}, // 0
  {B00000000, B00010000, B00110000, B00010000, B00010000, B00010000, B00010000, B00111000}, // 1
  {B00000000, B00111000, B01000100, B00000100, B00001000, B00010000, B00100000, B01111100}, // 2
  {B00000000, B01111100, B00001000, B00010000, B00001000, B00000100, B01000100, B00111000}, // 3
  {B00000000, B00001000, B00011000, B00101000, B01001000, B01111100, B00001000, B00001000}, // 4
  {B00000000, B01111100, B01000000, B01111000, B00000100, B00000100, B01000100, B00111000}, // 5
  {B00000000, B00011000, B00100000, B01000000, B01111000, B01000100, B01000100, B00111000}, // 6
  {B00000000, B01111100, B00000100, B00001000, B00010000, B00100000, B01000000, B01000000}, // 7
  {B00000000, B00111000, B01000100, B01000100, B00111000, B01000100, B01000100, B00111000}, // 8
  {B00000000, B00111000, B01000100, B01000100, B00111100, B00000100, B00001000, B00110000}, // 9 - 10
  {B00000000, B00111000, B01000100, B01000100, B01111100, B01000100, B01000100, B01000100}, // A
  {B00000000, B01111000, B01000100, B01000100, B01111000, B01000100, B01000100, B01111000}, // B
  {B00000000, B00111000, B01000100, B01000000, B01000000, B01000000, B01000100, B00111000}, // C
  {B00000000, B01111000, B01000100, B01000100, B01000100, B01000100, B01000100, B01111000}, // D
  {B00000000, B01111100, B01000000, B01000000, B01111000, B01000000, B01000000, B01111100}, // E
  {B00000000, B01111100, B01000000, B01000000, B01111000, B01000000, B01000000, B01000000}, // F
  {B00000000, B00111000, B01000100, B01000000, B01000000, B01001100, B01000100, B00111000}, // G
  {B00000000, B01000100, B01000100, B01000100, B01111100, B01000100, B01000100, B01000100}, // H
  {B00000000, B00111000, B00010000, B00010000, B00010000, B00010000, B00010000, B00111000}, // I
  {B00000000, B00011100, B00001000, B00001000, B00001000, B00001000, B01001000, B00110000}, // J - 20
  {B00000000, B01000100, B01001000, B01010000, B01100000, B01010000, B01001000, B01000100}, // K
  {B00000000, B01000000, B01000000, B01000000, B01000000, B01000000, B01000000, B01111000}, // L
  {B00000000, B01000100, B01101100, B01010100, B01010100, B01000100, B01000100, B01000100}, // M
  {B00000000, B01000100, B01000100, B01100100, B01010100, B01001100, B01000100, B01000100}, // N
  {B00000000, B00111000, B01000100, B01000100, B01000100, B01000100, B01000100, B00111000}, // O
  {B00000000, B01111000, B01000100, B01000100, B01111000, B01000000, B01000000, B01000000}, // P
  {B00000000, B00111000, B01000100, B01000100, B01000100, B01010100, B01001000, B00110100}, // Q
  {B00000000, B01111000, B01000100, B01000100, B01111000, B01010000, B01001000, B01000100}, // R
  {B00000000, B00111100, B01000000, B01000000, B00111000, B00000100, B00000100, B01111000}, // S
  {B00000000, B01111100, B00010000, B00010000, B00010000, B00010000, B00010000, B00010000}, // T - 30
  {B00000000, B01000100, B01000100, B01000100, B01000100, B01000100, B01000100, B00111000}, // U
  {B00000000, B01000100, B01000100, B01000100, B01000100, B00101000, B00101000, B00010000}, // V
  {B00000000, B01000100, B01000100, B01000100, B01010100, B01010100, B01010100, B00101000}, // W
  {B00000000, B01000100, B01000100, B00101000, B00010000, B00101000, B01000100, B01000100}, // X
  {B00000000, B01000100, B01000100, B00101000, B00010000, B00010000, B00010000, B00010000}, // Y
  {B00000000, B01111100, B00000100, B00001000, B00010000, B00100000, B01000000, B01111100}, // Z
  {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000}, //space or unknown - 37
  {B00000000,B00000000,B01111000,B00001100,B01111100,B11001100,B01110110,B00000000}, // a
  {B11100000,B01100000,B01100000,B01111100,B01100110,B01100110,B11011100,B00000000}, // b
  {B00000000,B00000000,B01111000,B11001100,B11000000,B11001100,B01111000,B00000000}, // c - 40
  {B00011100,B00001100,B00001100,B01111100,B11001100,B11001100,B01110110,B00000000}, // d
  {B00000000,B00000000,B01111000,B11001100,B11111100,B11000000,B01111000,B00000000}, // e
  {B00111000,B01101100,B01100000,B11110000,B01100000,B01100000,B11110000,B00000000}, // f 
  {B00000000,B00000000,B01110110,B11001100,B11001100,B01111100,B00001100,B11111000}, // g
  {B11100000,B01100000,B01101100,B01110110,B01100110,B01100110,B11100110,B00000000}, // h
  {B00110000,B00000000,B01110000,B00110000,B00110000,B00110000,B01111000,B00000000}, // i
  {B00001100,B00000000,B00001100,B00001100,B00001100,B11001100,B11001100,B01111000}, // j
  {B11100000,B01100000,B01100110,B01101100,B01111000,B01101100,B11100110,B00000000}, // k
  {B01110000,B00110000,B00110000,B00110000,B00110000,B00110000,B01111000,B00000000}, // l
  {B00000000,B00000000,B11001100,B11111110,B11111110,B11010110,B11000110,B00000000}, // m - 50
  {B00000000,B00000000,B11111000,B11001100,B11001100,B11001100,B11001100,B00000000}, // n
  {B00000000,B00000000,B01111000,B11001100,B11001100,B11001100,B01111000,B00000000}, // o
  {B00000000,B00000000,B11011100,B01100110,B01100110,B01111100,B01100000,B11110000}, // p
  {B00000000,B00000000,B01110110,B11001100,B11001100,B01111100,B00001100,B00011110}, // q
  {B00000000,B00000000,B10011100,B01110110,B01100110,B01100000,B11110000,B00000000}, // r
  {B00000000,B00000000,B01111100,B11000000,B01111000,B00001100,B11111000,B00000000}, // s
  {B00010000,B00110000,B01111100,B00110000,B00110000,B00110100,B00011000,B00000000}, // t
  {B00000000,B00000000,B11001100,B11001100,B11001100,B11001100,B01110110,B00000000}, // u
  {B00000000,B00000000,B11001100,B11001100,B11001100,B01111000,B00110000,B00000000}, // v
  {B00000000,B00000000,B11000110,B11000110,B11010110,B11111110,B01101100,B00000000}, // w - 60
  {B00000000,B00000000,B11000110,B01101100,B00111000,B01101100,B11000110,B00000000}, // x
  {B00000000,B00000000,B11001100,B11001100,B11001100,B01111100,B00001100,B11111000}, // y
  {B00000000,B00000000,B11111100,B10011000,B00110000,B01100100,B11111100,B00000000}, // z - 63
  {B00000000, B00100000, B00110000, B00101000, B00100100, B00100011, B01000000, B10001000}, // #
  {B00000000, B00000100, B00001100, B00010100, B00100100, B11000100, B00000010, B00010001}, // $
  {B00000000, B00000100, B00001100, B00010100, B00100100, B00100011, B01000000, B10001000}, // %
  {B00000000, B00100000, B00110000, B00101000, B00100100, B11000100, B00000010, B00010001} // &
};

String myStr = "            aaaaaaaaaa    ";
String myHiddenStr = "            aaaaaaaaaa    ";
String opt = "";

int counter = 0;
int wrt = 0;
int written = 0;
int ctrl = 0;
int pause = 0;
int logo = 0;

unsigned long strtCtrl;
unsigned long endCtrl;


void showdisplayBuffer()
{
  for (int n = 0; n < NB_MAX7219; n++) {
    for (int l = 0; l < 8; l++)
      lc.setRow(NB_MAX7219 - 1 - n, l, displayBuffer[8 * n + l]);
  }
}

void rotate90CW()
{
  byte tmpGrid[8];
  for (int n = 0; n < NB_MAX7219; n++) {
    memset ( tmpGrid, 0, sizeof(tmpGrid));
    for (byte r = 0; r < 8; r++)
      for (byte b = 0; b < 8; b++)
        if (bitRead(displayBuffer[8 * n + b], r)) bitSet(tmpGrid[7 - r], b);
    for (byte r = 0; r < 8; r++) displayBuffer[8 * n + r] = tmpGrid[r];
  }
}

void rotate90CCW()
{
  byte tmpGrid[8];
  for (int n = 0; n < NB_MAX7219; n++) {
    memset ( tmpGrid, 0, sizeof(tmpGrid));
    for (byte r = 0; r < 8; r++)
      for (byte b = 0; b < 8; b++)
        if (bitRead(displayBuffer[8 * n + 7 - b], r)) bitSet(tmpGrid[r], b);
    for (byte r = 0; r < 8; r++) displayBuffer[8 * n + r] = tmpGrid[r];
  }
}


void pushChar(const char aChar, unsigned long scrollSpeed)
{
  byte currentPattern[8];
  byte tmpGrid[8];

  if ((aChar >= '0') && (aChar <= '9')) {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - '0'][j];
  } else if ((aChar >= 'A') && (aChar <= 'Z')) {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - 'A' + 10][j];
  } else if ((aChar >= 'a') && (aChar <= 'z')) {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - 'a' + 37][j];
  } else if ((aChar >= '#') && (aChar <= '&')) {
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[aChar - '#' + 63][j];
  } else
    for (int j = 0; j < 8; j++) currentPattern[j] = alphabet[36][j];

  memset ( tmpGrid, 0, sizeof(tmpGrid));
  for (byte r = 0; r < 8; r++)
    for (byte b = 0; b < 8; b++)
      if (bitRead(currentPattern[b], r)) bitSet(tmpGrid[7 - r], b);
  for (byte r = 0; r < 8; r++) currentPattern[r] = tmpGrid[r];

  for (byte r = 0; r < 8; r++) {
    rotate90CW();
    for (int l = 1; l < 8 * NB_MAX7219; l++) displayBuffer[l - 1] = displayBuffer[l];
    displayBuffer[8 * NB_MAX7219 - 1] = currentPattern[r];
    rotate90CCW();
    showdisplayBuffer(); delay(scrollSpeed);
  }
}

void scrollTxt(const char * aString, unsigned long scrollSpeed, bool preloadDisplay)
{
  int strLength = strlen(aString);
  int currentChar = 0;

  memset (displayBuffer, 0, sizeof(displayBuffer));
  if (preloadDisplay) {
    // preload the display
    for (currentChar = 0; currentChar < NB_MAX7219; currentChar++) {
      if (currentChar < strLength) {
        if ((aString[currentChar] >= '0') && (aString[currentChar] <= '9')) {
          for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - '0'][j];
        } else if ((aString[currentChar] >= 'A') && (aString[currentChar] <= 'Z')) {
          for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - 'A' + 10][j];
        } else if ((aString[currentChar] >= 'a') && (aString[currentChar] <= 'z')) {
          for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - 'a' + 37][j];
        } else if ((aString[currentChar] >= '#') && (aString[currentChar] <= '&')) {
          for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[aString[currentChar] - '#' + 63][j];
        } else
          for (int j = 0; j < 8; j++) displayBuffer[8 * currentChar + j] = alphabet[36][j];
      }
    }
    showdisplayBuffer(); delay(scrollSpeed * 4ul);
  }
  
  if(pause == 0){
    while (currentChar < strLength + NB_MAX7219) {
      byte currentPattern[8];
      byte tmpGrid[8];
      if ( currentChar < strLength) pushChar(aString[currentChar], scrollSpeed);
      //else pushChar(' ', scrollSpeed); // pad with spaces
      currentChar++;
    }
  }
  
}


void setup()
{
  Serial.begin(9600);
  for (int index = 0; index < NB_MAX7219; index++) { // NB_MAX7219 similar to lc.getDeviceCount()
    lc.shutdown(index, false);
    lc.setIntensity(index, 4); // (0~15)
    lc.clearDisplay(index);
  }
}


void loop()
{
  if (Serial.available()) {
    
    if(wrt == 0){
      opt = Serial.readStringUntil('!');  
    }else{
      opt = Serial.readStringUntil('*');
      wrt = 0;
      written = 1;
    }
    
    opt.replace("\n", "");

    if(ctrl == 0){
      if(opt == "control"){
        Serial.println("");
        ctrl = 1;
        strtCtrl = millis();
        Serial.println("control!");
      } else if(opt == "pause"){
        Serial.println("pause!");
        pause = 0;
        Serial.println("OK!");    
      }
      
      if(written == 1){
        myHiddenStr = "            " + opt.substring(0,10) + "    ";
        Serial.println(myHiddenStr);
        written = 0;
        Serial.println("OK!");
      }
    } else {
      
      if(opt == "write"){
          wrt = 1;
          Serial.println("write!");
          ctrl = 0;
          
      } else if(opt == "blank"){
          Serial.println("blank!");
          myStr = "                      ";
          Serial.println("OK!");
          ctrl = 0;

          if(logo == 1){
            logo = 0;
          }
          
      } else if(opt == "pause"){
          Serial.println("pause!");
          pause = 1;
          ctrl = 0;
          
      } else if(opt == "show"){
          Serial.println("show!");
          Serial.println(myHiddenStr);
          myStr = myHiddenStr;
          Serial.println("OK!");
          ctrl = 0;

          if(logo == 1){
            logo = 0;
          }
          
      } else if(opt == "logo"){
          Serial.println("logo!");
          ctrl = 0;
          logo = 1;
          Serial.println("OK!");
      } else {
        endCtrl = millis();
        if((endCtrl - strtCtrl) >= 10000){
          ctrl = 0;
        }
      }
    }
    
  } else {
    if(logo == 1 && pause == 0){
      if(counter == 0){
        myStr = "            #$";
        counter = 1;
      }else{
        myStr = "            %&";
        counter = 0;
      }
    }
  
    int strLen = myStr.length()+1;
    char sentence[strLen];
    myStr.toCharArray(sentence, strLen);
    
    scrollTxt(sentence, 2ul, true);
    //delay(50);
  }
  
}
