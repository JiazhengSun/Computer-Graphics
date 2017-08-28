#define PROCESSING_COLOR_SHADER
//Jiazheng Sun
#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  float cx = vertTexCoord.s *3.0 - 2.1;
  float cy = vertTexCoord.t * 3.0 - 1.5;
  vec2 z = vec2(0,0);
  for (int index = 0; index < 20; index++) {
  	 float newReal = pow(z.x,2) - pow(z.y,2) + cx;
  	 float newImag = 2.0 * z.x * z.y + cy;
  	 z = vec2(newReal,newImag);
  }
  if (pow(z.x,2)+ pow(z.y,2) < 4) {
  	gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
  } else {
  	gl_FragColor = vec4(0.1,0.6,0.3,1.0);
  }
}

