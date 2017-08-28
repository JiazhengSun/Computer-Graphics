#define PROCESSING_COLOR_SHADER
//Jiazheng Sun

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	float r = 0.1;
	float x_distance = 0.0;
	float y_distance = 0.0;
	if (vertTexCoord.t < (1.0/3)) { //First row
		y_distance = pow((vertTexCoord.t -(0.5/3)),2);
		if (vertTexCoord.s < (1.0/3)) { //First column
			x_distance = pow((vertTexCoord.s - (0.5/3)),2); //circle center(0.5/3,0.5/3)
		} else if (vertTexCoord.s < (2.0/3)) { // Second column
			x_distance = pow((vertTexCoord.s - 0.5),2); //circle center(0.5,0.5/3)
		} else { //Third column
			x_distance = pow((vertTexCoord.s - (2.5/3)),2);
		}
	} else if (vertTexCoord.t < (2.0/3)) { //Second row
		y_distance = pow((vertTexCoord.t - 0.5),2);
		if (vertTexCoord.s < (1.0/3)) { //First column
			x_distance = pow((vertTexCoord.s - (0.5/3)),2); //circle center(0.5/3,0.5/3)
		} else if (vertTexCoord.s < (2.0/3)) { // Second column
			x_distance = pow((vertTexCoord.s - 0.5),2); //circle center(0.5,0.5/3)
		} else{ //Third column
			x_distance = pow((vertTexCoord.s - (2.5/3)),2);
		}
	} else { //third column
		y_distance = pow((vertTexCoord.t - (2.5/3)),2);
		if (vertTexCoord.s < (1.0/3)) { //First column
			x_distance = pow((vertTexCoord.s - (0.5/3)),2); //circle center(0.5/3,0.5/3)
		} else if (vertTexCoord.s < (2.0/3)) { // Second column
			x_distance = pow((vertTexCoord.s - 0.5),2); //circle center(0.5,0.5/3)
		} else{ //Third column
			x_distance = pow((vertTexCoord.s - (2.5/3)),2);
		}
	}
	if (x_distance + y_distance <= pow(r,2)) { // in the circle
		gl_FragColor = vec4(0.2, 0.4, 1.0, 0);
	} else {
		gl_FragColor = vec4(0.2, 0.4, 1.0, 0.5);
	}

}

