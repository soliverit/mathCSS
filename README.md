# mathCSS-py

A python CSS factory for Math and Plotting in vanilla CSS. 

  Math stuff: Power, Product, Sum, Sin, Cos, Tan, Distance, SimpleLinearRegression, BallisticFormula 
#### Why?
Slow news day

### Notes

  CSS doesn't support functions or go tos which means code cannot be reused. Every point is a replica
  of the function that's being worked out. The two blocks in the example show what a point looks like.
  
  In the examples, An HTML file is created with styleless divs for each point. All properties are applied
  in the CSS block.

**Simple linear regression** (see <a href="https://github.com/soliverit/mathCSS/blob/main/test/slg_style.css">"./test/slg_style.css"</a> - 28,000~ lines)

<img src="https://i.imgur.com/ae4MW9G.png" style="float: left; margin-right: 10px;width:400px;height:350px;" />

**Sample point**

```css
#lin-0{
--lin-0-x0: 0; --lin-0-y0: 2;
--lin-0-x1: 2; --lin-0-y1: 4;
--lin-0-x2: 4; --lin-0-y2: 3;
--lin-0-x3: 6; --lin-0-y3: 4;
--lin-0-x4: 8; --lin-0-y4: 7;
--lin-0-x5: 10; --lin-0-y5: 8;
--lin-0-x6: 12; --lin-0-y6: 7;
--lin-0-x7: 14; --lin-0-y7: 9;
--lin-0-x8: 16; --lin-0-y8: 10;
--lin-0-x9: 18; --lin-0-y9: 10;
--lin-0-x10: 20; --lin-0-y10: 11;
--lin-0-x11: 22; --lin-0-y11: 13;
--lin-0-x12: 24; --lin-0-y12: 14;
--lin-0-x13: 26; --lin-0-y13: 15;
--lin-0-x14: 28; --lin-0-y14: 17;
--lin-0-x15: 30; --lin-0-y15: 16;
--lin-0-x16: 32; --lin-0-y16: 17;
--lin-0-x17: 34; --lin-0-y17: 20;
--lin-0-x18: 36; --lin-0-y18: 21;
--lin-0-x19: 38; --lin-0-y19: 21;
--lin-0-x20: 40; --lin-0-y20: 22;
--lin-0-x21: 42; --lin-0-y21: 24;
--lin-0-x22: 44; --lin-0-y22: 23;
--lin-0-x23: 46; --lin-0-y23: 26;
--lin-0-x24: 48; --lin-0-y24: 26;
--lin-0-x25: 50; --lin-0-y25: 27;
--lin-0-x26: 52; --lin-0-y26: 29;
--lin-0-x27: 54; --lin-0-y27: 30;
--lin-0-x28: 56; --lin-0-y28: 31;
--lin-0-x29: 58; --lin-0-y29: 32;
--lin-0-x30: 60; --lin-0-y30: 31;
--lin-0-x31: 62; --lin-0-y31: 32;
--lin-0-x32: 64; --lin-0-y32: 34;
--lin-0-x33: 66; --lin-0-y33: 34;
--lin-0-x34: 68; --lin-0-y34: 37;
--lin-0-x35: 70; --lin-0-y35: 38;
--lin-0-x36: 72; --lin-0-y36: 38;
--lin-0-x37: 74; --lin-0-y37: 38;
--lin-0-x38: 76; --lin-0-y38: 39;
--lin-0-x39: 78; --lin-0-y39: 42;
--lin-0-x40: 80; --lin-0-y40: 41;
--lin-0-x41: 82; --lin-0-y41: 43;
--lin-0-x42: 84; --lin-0-y42: 44;
--lin-0-x43: 86; --lin-0-y43: 46;
--lin-0-x44: 88; --lin-0-y44: 47;
--lin-0-x45: 90; --lin-0-y45: 47;
--lin-0-x46: 92; --lin-0-y46: 48;
--lin-0-x47: 94; --lin-0-y47: 49;
--lin-0-x48: 96; --lin-0-y48: 50;
--lin-0-x49: 98; --lin-0-y49: 50;
--lin-0-mean-x: calc((var(--lin-0-x0) + var(--lin-0-x1) + var(--lin-0-x2) + var(--lin-0-x3) + var(--lin-0-x4) + var(--lin-0-x5) + var(--lin-0-x6) + var(--lin-0-x7) + var(--lin-0-x8) + var(--lin-0-x9) + var(--lin-0-x10) + var(--lin-0-x11) + var(--lin-0-x12) + var(--lin-0-x13) + var(--lin-0-x14) + var(--lin-0-x15) + var(--lin-0-x16) + var(--lin-0-x17) + var(--lin-0-x18) + var(--lin-0-x19) + var(--lin-0-x20) + var(--lin-0-x21) + var(--lin-0-x22) + var(--lin-0-x23) + var(--lin-0-x24) + var(--lin-0-x25) + var(--lin-0-x26) + var(--lin-0-x27) + var(--lin-0-x28) + var(--lin-0-x29) + var(--lin-0-x30) + var(--lin-0-x31) + var(--lin-0-x32) + var(--lin-0-x33) + var(--lin-0-x34) + var(--lin-0-x35) + var(--lin-0-x36) + var(--lin-0-x37) + var(--lin-0-x38) + var(--lin-0-x39) + var(--lin-0-x40) + var(--lin-0-x41) + var(--lin-0-x42) + var(--lin-0-x43) + var(--lin-0-x44) + var(--lin-0-x45) + var(--lin-0-x46) + var(--lin-0-x47) + var(--lin-0-x48) + var(--lin-0-x49)) / 50);
--lin-0-mean-y: calc((var(--lin-0-y0) + var(--lin-0-y1) + var(--lin-0-y2) + var(--lin-0-y3) + var(--lin-0-y4) + var(--lin-0-y5) + var(--lin-0-y6) + var(--lin-0-y7) + var(--lin-0-y8) + var(--lin-0-y9) + var(--lin-0-y10) + var(--lin-0-y11) + var(--lin-0-y12) + var(--lin-0-y13) + var(--lin-0-y14) + var(--lin-0-y15) + var(--lin-0-y16) + var(--lin-0-y17) + var(--lin-0-y18) + var(--lin-0-y19) + var(--lin-0-y20) + var(--lin-0-y21) + var(--lin-0-y22) + var(--lin-0-y23) + var(--lin-0-y24) + var(--lin-0-y25) + var(--lin-0-y26) + var(--lin-0-y27) + var(--lin-0-y28) + var(--lin-0-y29) + var(--lin-0-y30) + var(--lin-0-y31) + var(--lin-0-y32) + var(--lin-0-y33) + var(--lin-0-y34) + var(--lin-0-y35) + var(--lin-0-y36) + var(--lin-0-y37) + var(--lin-0-y38) + var(--lin-0-y39) + var(--lin-0-y40) + var(--lin-0-y41) + var(--lin-0-y42) + var(--lin-0-y43) + var(--lin-0-y44) + var(--lin-0-y45) + var(--lin-0-y46) + var(--lin-0-y47) + var(--lin-0-y48) + var(--lin-0-y49)) / 50);
--lin-0-err-x0: calc(var(--lin-0-x0) - var(--lin-0-mean-x));
--lin-0-err-y0: calc(var(--lin-0-y0) - var(--lin-0-mean-y));
--lin-0-err-x1: calc(var(--lin-0-x1) - var(--lin-0-mean-x));
--lin-0-err-y1: calc(var(--lin-0-y1) - var(--lin-0-mean-y));
--lin-0-err-x2: calc(var(--lin-0-x2) - var(--lin-0-mean-x));
--lin-0-err-y2: calc(var(--lin-0-y2) - var(--lin-0-mean-y));
--lin-0-err-x3: calc(var(--lin-0-x3) - var(--lin-0-mean-x));
--lin-0-err-y3: calc(var(--lin-0-y3) - var(--lin-0-mean-y));
--lin-0-err-x4: calc(var(--lin-0-x4) - var(--lin-0-mean-x));
--lin-0-err-y4: calc(var(--lin-0-y4) - var(--lin-0-mean-y));
--lin-0-err-x5: calc(var(--lin-0-x5) - var(--lin-0-mean-x));
--lin-0-err-y5: calc(var(--lin-0-y5) - var(--lin-0-mean-y));
--lin-0-err-x6: calc(var(--lin-0-x6) - var(--lin-0-mean-x));
--lin-0-err-y6: calc(var(--lin-0-y6) - var(--lin-0-mean-y));
--lin-0-err-x7: calc(var(--lin-0-x7) - var(--lin-0-mean-x));
--lin-0-err-y7: calc(var(--lin-0-y7) - var(--lin-0-mean-y));
--lin-0-err-x8: calc(var(--lin-0-x8) - var(--lin-0-mean-x));
--lin-0-err-y8: calc(var(--lin-0-y8) - var(--lin-0-mean-y));
--lin-0-err-x9: calc(var(--lin-0-x9) - var(--lin-0-mean-x));
--lin-0-err-y9: calc(var(--lin-0-y9) - var(--lin-0-mean-y));
--lin-0-err-x10: calc(var(--lin-0-x10) - var(--lin-0-mean-x));
--lin-0-err-y10: calc(var(--lin-0-y10) - var(--lin-0-mean-y));
--lin-0-err-x11: calc(var(--lin-0-x11) - var(--lin-0-mean-x));
--lin-0-err-y11: calc(var(--lin-0-y11) - var(--lin-0-mean-y));
--lin-0-err-x12: calc(var(--lin-0-x12) - var(--lin-0-mean-x));
--lin-0-err-y12: calc(var(--lin-0-y12) - var(--lin-0-mean-y));
--lin-0-err-x13: calc(var(--lin-0-x13) - var(--lin-0-mean-x));
--lin-0-err-y13: calc(var(--lin-0-y13) - var(--lin-0-mean-y));
--lin-0-err-x14: calc(var(--lin-0-x14) - var(--lin-0-mean-x));
--lin-0-err-y14: calc(var(--lin-0-y14) - var(--lin-0-mean-y));
--lin-0-err-x15: calc(var(--lin-0-x15) - var(--lin-0-mean-x));
--lin-0-err-y15: calc(var(--lin-0-y15) - var(--lin-0-mean-y));
--lin-0-err-x16: calc(var(--lin-0-x16) - var(--lin-0-mean-x));
--lin-0-err-y16: calc(var(--lin-0-y16) - var(--lin-0-mean-y));
--lin-0-err-x17: calc(var(--lin-0-x17) - var(--lin-0-mean-x));
--lin-0-err-y17: calc(var(--lin-0-y17) - var(--lin-0-mean-y));
--lin-0-err-x18: calc(var(--lin-0-x18) - var(--lin-0-mean-x));
--lin-0-err-y18: calc(var(--lin-0-y18) - var(--lin-0-mean-y));
--lin-0-err-x19: calc(var(--lin-0-x19) - var(--lin-0-mean-x));
--lin-0-err-y19: calc(var(--lin-0-y19) - var(--lin-0-mean-y));
--lin-0-err-x20: calc(var(--lin-0-x20) - var(--lin-0-mean-x));
--lin-0-err-y20: calc(var(--lin-0-y20) - var(--lin-0-mean-y));
--lin-0-err-x21: calc(var(--lin-0-x21) - var(--lin-0-mean-x));
--lin-0-err-y21: calc(var(--lin-0-y21) - var(--lin-0-mean-y));
--lin-0-err-x22: calc(var(--lin-0-x22) - var(--lin-0-mean-x));
--lin-0-err-y22: calc(var(--lin-0-y22) - var(--lin-0-mean-y));
--lin-0-err-x23: calc(var(--lin-0-x23) - var(--lin-0-mean-x));
--lin-0-err-y23: calc(var(--lin-0-y23) - var(--lin-0-mean-y));
--lin-0-err-x24: calc(var(--lin-0-x24) - var(--lin-0-mean-x));
--lin-0-err-y24: calc(var(--lin-0-y24) - var(--lin-0-mean-y));
--lin-0-err-x25: calc(var(--lin-0-x25) - var(--lin-0-mean-x));
--lin-0-err-y25: calc(var(--lin-0-y25) - var(--lin-0-mean-y));
--lin-0-err-x26: calc(var(--lin-0-x26) - var(--lin-0-mean-x));
--lin-0-err-y26: calc(var(--lin-0-y26) - var(--lin-0-mean-y));
--lin-0-err-x27: calc(var(--lin-0-x27) - var(--lin-0-mean-x));
--lin-0-err-y27: calc(var(--lin-0-y27) - var(--lin-0-mean-y));
--lin-0-err-x28: calc(var(--lin-0-x28) - var(--lin-0-mean-x));
--lin-0-err-y28: calc(var(--lin-0-y28) - var(--lin-0-mean-y));
--lin-0-err-x29: calc(var(--lin-0-x29) - var(--lin-0-mean-x));
--lin-0-err-y29: calc(var(--lin-0-y29) - var(--lin-0-mean-y));
--lin-0-err-x30: calc(var(--lin-0-x30) - var(--lin-0-mean-x));
--lin-0-err-y30: calc(var(--lin-0-y30) - var(--lin-0-mean-y));
--lin-0-err-x31: calc(var(--lin-0-x31) - var(--lin-0-mean-x));
--lin-0-err-y31: calc(var(--lin-0-y31) - var(--lin-0-mean-y));
--lin-0-err-x32: calc(var(--lin-0-x32) - var(--lin-0-mean-x));
--lin-0-err-y32: calc(var(--lin-0-y32) - var(--lin-0-mean-y));
--lin-0-err-x33: calc(var(--lin-0-x33) - var(--lin-0-mean-x));
--lin-0-err-y33: calc(var(--lin-0-y33) - var(--lin-0-mean-y));
--lin-0-err-x34: calc(var(--lin-0-x34) - var(--lin-0-mean-x));
--lin-0-err-y34: calc(var(--lin-0-y34) - var(--lin-0-mean-y));
--lin-0-err-x35: calc(var(--lin-0-x35) - var(--lin-0-mean-x));
--lin-0-err-y35: calc(var(--lin-0-y35) - var(--lin-0-mean-y));
--lin-0-err-x36: calc(var(--lin-0-x36) - var(--lin-0-mean-x));
--lin-0-err-y36: calc(var(--lin-0-y36) - var(--lin-0-mean-y));
--lin-0-err-x37: calc(var(--lin-0-x37) - var(--lin-0-mean-x));
--lin-0-err-y37: calc(var(--lin-0-y37) - var(--lin-0-mean-y));
--lin-0-err-x38: calc(var(--lin-0-x38) - var(--lin-0-mean-x));
--lin-0-err-y38: calc(var(--lin-0-y38) - var(--lin-0-mean-y));
--lin-0-err-x39: calc(var(--lin-0-x39) - var(--lin-0-mean-x));
--lin-0-err-y39: calc(var(--lin-0-y39) - var(--lin-0-mean-y));
--lin-0-err-x40: calc(var(--lin-0-x40) - var(--lin-0-mean-x));
--lin-0-err-y40: calc(var(--lin-0-y40) - var(--lin-0-mean-y));
--lin-0-err-x41: calc(var(--lin-0-x41) - var(--lin-0-mean-x));
--lin-0-err-y41: calc(var(--lin-0-y41) - var(--lin-0-mean-y));
--lin-0-err-x42: calc(var(--lin-0-x42) - var(--lin-0-mean-x));
--lin-0-err-y42: calc(var(--lin-0-y42) - var(--lin-0-mean-y));
--lin-0-err-x43: calc(var(--lin-0-x43) - var(--lin-0-mean-x));
--lin-0-err-y43: calc(var(--lin-0-y43) - var(--lin-0-mean-y));
--lin-0-err-x44: calc(var(--lin-0-x44) - var(--lin-0-mean-x));
--lin-0-err-y44: calc(var(--lin-0-y44) - var(--lin-0-mean-y));
--lin-0-err-x45: calc(var(--lin-0-x45) - var(--lin-0-mean-x));
--lin-0-err-y45: calc(var(--lin-0-y45) - var(--lin-0-mean-y));
--lin-0-err-x46: calc(var(--lin-0-x46) - var(--lin-0-mean-x));
--lin-0-err-y46: calc(var(--lin-0-y46) - var(--lin-0-mean-y));
--lin-0-err-x47: calc(var(--lin-0-x47) - var(--lin-0-mean-x));
--lin-0-err-y47: calc(var(--lin-0-y47) - var(--lin-0-mean-y));
--lin-0-err-x48: calc(var(--lin-0-x48) - var(--lin-0-mean-x));
--lin-0-err-y48: calc(var(--lin-0-y48) - var(--lin-0-mean-y));
--lin-0-err-x49: calc(var(--lin-0-x49) - var(--lin-0-mean-x));
--lin-0-err-y49: calc(var(--lin-0-y49) - var(--lin-0-mean-y));
--lin-0-err-s: calc(var(--lin-0-err-x0) * var(--lin-0-err-x0) + var(--lin-0-err-x1) * var(--lin-0-err-x1) + var(--lin-0-err-x2) * var(--lin-0-err-x2) + var(--lin-0-err-x3) * var(--lin-0-err-x3) + var(--lin-0-err-x4) * var(--lin-0-err-x4) + var(--lin-0-err-x5) * var(--lin-0-err-x5) + var(--lin-0-err-x6) * var(--lin-0-err-x6) + var(--lin-0-err-x7) * var(--lin-0-err-x7) + var(--lin-0-err-x8) * var(--lin-0-err-x8) + var(--lin-0-err-x9) * var(--lin-0-err-x9) + var(--lin-0-err-x10) * var(--lin-0-err-x10) + var(--lin-0-err-x11) * var(--lin-0-err-x11) + var(--lin-0-err-x12) * var(--lin-0-err-x12) + var(--lin-0-err-x13) * var(--lin-0-err-x13) + var(--lin-0-err-x14) * var(--lin-0-err-x14) + var(--lin-0-err-x15) * var(--lin-0-err-x15) + var(--lin-0-err-x16) * var(--lin-0-err-x16) + var(--lin-0-err-x17) * var(--lin-0-err-x17) + var(--lin-0-err-x18) * var(--lin-0-err-x18) + var(--lin-0-err-x19) * var(--lin-0-err-x19) + var(--lin-0-err-x20) * var(--lin-0-err-x20) + var(--lin-0-err-x21) * var(--lin-0-err-x21) + var(--lin-0-err-x22) * var(--lin-0-err-x22) + var(--lin-0-err-x23) * var(--lin-0-err-x23) + var(--lin-0-err-x24) * var(--lin-0-err-x24) + var(--lin-0-err-x25) * var(--lin-0-err-x25) + var(--lin-0-err-x26) * var(--lin-0-err-x26) + var(--lin-0-err-x27) * var(--lin-0-err-x27) + var(--lin-0-err-x28) * var(--lin-0-err-x28) + var(--lin-0-err-x29) * var(--lin-0-err-x29) + var(--lin-0-err-x30) * var(--lin-0-err-x30) + var(--lin-0-err-x31) * var(--lin-0-err-x31) + var(--lin-0-err-x32) * var(--lin-0-err-x32) + var(--lin-0-err-x33) * var(--lin-0-err-x33) + var(--lin-0-err-x34) * var(--lin-0-err-x34) + var(--lin-0-err-x35) * var(--lin-0-err-x35) + var(--lin-0-err-x36) * var(--lin-0-err-x36) + var(--lin-0-err-x37) * var(--lin-0-err-x37) + var(--lin-0-err-x38) * var(--lin-0-err-x38) + var(--lin-0-err-x39) * var(--lin-0-err-x39) + var(--lin-0-err-x40) * var(--lin-0-err-x40) + var(--lin-0-err-x41) * var(--lin-0-err-x41) + var(--lin-0-err-x42) * var(--lin-0-err-x42) + var(--lin-0-err-x43) * var(--lin-0-err-x43) + var(--lin-0-err-x44) * var(--lin-0-err-x44) + var(--lin-0-err-x45) * var(--lin-0-err-x45) + var(--lin-0-err-x46) * var(--lin-0-err-x46) + var(--lin-0-err-x47) * var(--lin-0-err-x47) + var(--lin-0-err-x48) * var(--lin-0-err-x48) + var(--lin-0-err-x49) * var(--lin-0-err-x49));
--lin-0-err-x-s0: calc(var(--lin-0-err-x0) * var(--lin-0-err-y0));
--lin-0-err-x-s1: calc(var(--lin-0-err-x1) * var(--lin-0-err-y1));
--lin-0-err-x-s2: calc(var(--lin-0-err-x2) * var(--lin-0-err-y2));
--lin-0-err-x-s3: calc(var(--lin-0-err-x3) * var(--lin-0-err-y3));
--lin-0-err-x-s4: calc(var(--lin-0-err-x4) * var(--lin-0-err-y4));
--lin-0-err-x-s5: calc(var(--lin-0-err-x5) * var(--lin-0-err-y5));
--lin-0-err-x-s6: calc(var(--lin-0-err-x6) * var(--lin-0-err-y6));
--lin-0-err-x-s7: calc(var(--lin-0-err-x7) * var(--lin-0-err-y7));
--lin-0-err-x-s8: calc(var(--lin-0-err-x8) * var(--lin-0-err-y8));
--lin-0-err-x-s9: calc(var(--lin-0-err-x9) * var(--lin-0-err-y9));
--lin-0-err-x-s10: calc(var(--lin-0-err-x10) * var(--lin-0-err-y10));
--lin-0-err-x-s11: calc(var(--lin-0-err-x11) * var(--lin-0-err-y11));
--lin-0-err-x-s12: calc(var(--lin-0-err-x12) * var(--lin-0-err-y12));
--lin-0-err-x-s13: calc(var(--lin-0-err-x13) * var(--lin-0-err-y13));
--lin-0-err-x-s14: calc(var(--lin-0-err-x14) * var(--lin-0-err-y14));
--lin-0-err-x-s15: calc(var(--lin-0-err-x15) * var(--lin-0-err-y15));
--lin-0-err-x-s16: calc(var(--lin-0-err-x16) * var(--lin-0-err-y16));
--lin-0-err-x-s17: calc(var(--lin-0-err-x17) * var(--lin-0-err-y17));
--lin-0-err-x-s18: calc(var(--lin-0-err-x18) * var(--lin-0-err-y18));
--lin-0-err-x-s19: calc(var(--lin-0-err-x19) * var(--lin-0-err-y19));
--lin-0-err-x-s20: calc(var(--lin-0-err-x20) * var(--lin-0-err-y20));
--lin-0-err-x-s21: calc(var(--lin-0-err-x21) * var(--lin-0-err-y21));
--lin-0-err-x-s22: calc(var(--lin-0-err-x22) * var(--lin-0-err-y22));
--lin-0-err-x-s23: calc(var(--lin-0-err-x23) * var(--lin-0-err-y23));
--lin-0-err-x-s24: calc(var(--lin-0-err-x24) * var(--lin-0-err-y24));
--lin-0-err-x-s25: calc(var(--lin-0-err-x25) * var(--lin-0-err-y25));
--lin-0-err-x-s26: calc(var(--lin-0-err-x26) * var(--lin-0-err-y26));
--lin-0-err-x-s27: calc(var(--lin-0-err-x27) * var(--lin-0-err-y27));
--lin-0-err-x-s28: calc(var(--lin-0-err-x28) * var(--lin-0-err-y28));
--lin-0-err-x-s29: calc(var(--lin-0-err-x29) * var(--lin-0-err-y29));
--lin-0-err-x-s30: calc(var(--lin-0-err-x30) * var(--lin-0-err-y30));
--lin-0-err-x-s31: calc(var(--lin-0-err-x31) * var(--lin-0-err-y31));
--lin-0-err-x-s32: calc(var(--lin-0-err-x32) * var(--lin-0-err-y32));
--lin-0-err-x-s33: calc(var(--lin-0-err-x33) * var(--lin-0-err-y33));
--lin-0-err-x-s34: calc(var(--lin-0-err-x34) * var(--lin-0-err-y34));
--lin-0-err-x-s35: calc(var(--lin-0-err-x35) * var(--lin-0-err-y35));
--lin-0-err-x-s36: calc(var(--lin-0-err-x36) * var(--lin-0-err-y36));
--lin-0-err-x-s37: calc(var(--lin-0-err-x37) * var(--lin-0-err-y37));
--lin-0-err-x-s38: calc(var(--lin-0-err-x38) * var(--lin-0-err-y38));
--lin-0-err-x-s39: calc(var(--lin-0-err-x39) * var(--lin-0-err-y39));
--lin-0-err-x-s40: calc(var(--lin-0-err-x40) * var(--lin-0-err-y40));
--lin-0-err-x-s41: calc(var(--lin-0-err-x41) * var(--lin-0-err-y41));
--lin-0-err-x-s42: calc(var(--lin-0-err-x42) * var(--lin-0-err-y42));
--lin-0-err-x-s43: calc(var(--lin-0-err-x43) * var(--lin-0-err-y43));
--lin-0-err-x-s44: calc(var(--lin-0-err-x44) * var(--lin-0-err-y44));
--lin-0-err-x-s45: calc(var(--lin-0-err-x45) * var(--lin-0-err-y45));
--lin-0-err-x-s46: calc(var(--lin-0-err-x46) * var(--lin-0-err-y46));
--lin-0-err-x-s47: calc(var(--lin-0-err-x47) * var(--lin-0-err-y47));
--lin-0-err-x-s48: calc(var(--lin-0-err-x48) * var(--lin-0-err-y48));
--lin-0-err-x-s49: calc(var(--lin-0-err-x49) * var(--lin-0-err-y49));
--lin-0-B1: calc((var(--lin-0-err-x-s0) + 
	var(--lin-0-err-x-s1) + 
	var(--lin-0-err-x-s2) + 
	var(--lin-0-err-x-s3) + 
	var(--lin-0-err-x-s4) + 
	var(--lin-0-err-x-s5) + 
	var(--lin-0-err-x-s6) + 
	var(--lin-0-err-x-s7) + 
	var(--lin-0-err-x-s8) + 
	var(--lin-0-err-x-s9) + 
	var(--lin-0-err-x-s10) + 
	var(--lin-0-err-x-s11) + 
	var(--lin-0-err-x-s12) + 
	var(--lin-0-err-x-s13) + 
	var(--lin-0-err-x-s14) + 
	var(--lin-0-err-x-s15) + 
	var(--lin-0-err-x-s16) + 
	var(--lin-0-err-x-s17) + 
	var(--lin-0-err-x-s18) + 
	var(--lin-0-err-x-s19) + 
	var(--lin-0-err-x-s20) + 
	var(--lin-0-err-x-s21) + 
	var(--lin-0-err-x-s22) + 
	var(--lin-0-err-x-s23) + 
	var(--lin-0-err-x-s24) + 
	var(--lin-0-err-x-s25) + 
	var(--lin-0-err-x-s26) + 
	var(--lin-0-err-x-s27) + 
	var(--lin-0-err-x-s28) + 
	var(--lin-0-err-x-s29) + 
	var(--lin-0-err-x-s30) + 
	var(--lin-0-err-x-s31) + 
	var(--lin-0-err-x-s32) + 
	var(--lin-0-err-x-s33) + 
	var(--lin-0-err-x-s34) + 
	var(--lin-0-err-x-s35) + 
	var(--lin-0-err-x-s36) + 
	var(--lin-0-err-x-s37) + 
	var(--lin-0-err-x-s38) + 
	var(--lin-0-err-x-s39) + 
	var(--lin-0-err-x-s40) + 
	var(--lin-0-err-x-s41) + 
	var(--lin-0-err-x-s42) + 
	var(--lin-0-err-x-s43) + 
	var(--lin-0-err-x-s44) + 
	var(--lin-0-err-x-s45) + 
	var(--lin-0-err-x-s46) + 
	var(--lin-0-err-x-s47) + 
	var(--lin-0-err-x-s48) + 
	var(--lin-0-err-x-s49)) / var(--lin-0-err-s));
--lin-0: calc(0 * (var(--lin-0-mean-y) - var(--lin-0-B1) * var(--lin-0-mean-x)));

bottom:calc(1px * var(--lin-0));
height: 5px;
width: 5px;
left: 5px;
display: block;
position: absolute;
margin: 2px;
border: 1px solid black;
z-index: 10;
background: green;
}
```


**Trajectories** (see <a href="https://github.com/soliverit/mathCSS/blob/main/test/ball_style.css">"./test/ball_style.css"</a> - 950~ lines)

<img src="https://i.imgur.com/VJ6YuQn.png" style="float: left; margin-right: 10px;width:400px;height:350px;" />

**Sample point:**

```css
#ballistic-series0{
--ballistic-series0-half-number: -0.5;
--ballistic-series0-gravity: 5.5;
--ballistic-series0-time: 0;
--ballistic-series0-velocity: 57;
--ballistic-series0y-offset: 20;
--ballistic-series0-time-squared: calc(var(--ballistic-series0-time) * var(--ballistic-series0-time));
--ballistic-series0-y-property-0: var(--ballistic-series0-half-number);
--ballistic-series0-y-property-1: var(--ballistic-series0-gravity);
--ballistic-series0-y-property-2: var(--ballistic-series0-time-squared);
--ballistic-series0-y: calc(var(--ballistic-series0-y-property-0) * var(--ballistic-series0-y-property-1) * var(--ballistic-series0-y-property-2));
--ballistic-series0-vt-property-0: var(--ballistic-series0-velocity);
--ballistic-series0-vt-property-1: var(--ballistic-series0-time);
--ballistic-series0-vt: calc(var(--ballistic-series0-vt-property-0) * var(--ballistic-series0-vt-property-1));
----ballistic-series0-y-property-0: var(--ballistic-series0y-offset);
----ballistic-series0-y-property-1: var(--ballistic-series0-vt);
----ballistic-series0-y-property-2: var(--ballistic-series0-y);
----ballistic-series0-y: calc(var(----ballistic-series0-y-property-0) + var(----ballistic-series0-y-property-1) + var(----ballistic-series0-y-property-2));
--ballistic-series0: var(----ballistic-series0-y);

bottom:calc(1px * var(--ballistic-series0));
height: 5px;
width: 5px;
left: 5px;
display: block;
position: absolute;
margin: 2px;
border: 1px solid black;
z-index: 10;
background: green;
}
```
