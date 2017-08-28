#define PROCESSING_TEXTURE_SHADER
//Jiazheng Sun
#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  float original_R = diffuse_color.r * 0.3;
  float original_G = diffuse_color.g * 0.6;
  float original_B = diffuse_color.b * 0.1;
  float original_intensity = original_R + original_G + original_B;

  vec2 up_pixel = vec2(vertTexCoord.x, (vertTexCoord.y - (1.0/256)));
  vec4 up_color = texture2D(texture, up_pixel.xy);
  float up_intensity = up_color.r * 0.3 + up_color.g * 0.6 + up_color.b * 0.1;

  vec2 down_pixel = vec2(vertTexCoord.x, (vertTexCoord.y + (1.0/256)));
  vec4 down_color = texture2D(texture, down_pixel.xy);
  float down_intensity = down_color.r * 0.3 + down_color.g * 0.6 + down_color.b * 0.1;

  vec2 left_pixel = vec2((vertTexCoord.x - (1.0/256)),vertTexCoord.y);
  vec4 left_color = texture2D(texture, left_pixel.xy);
  float left_intensity = left_color.r * 0.3 + left_color.g * 0.6 + left_color.b * 0.1;

  vec2 right_pixel = vec2((vertTexCoord.x +(1.0/256)),vertTexCoord.y);
  vec4 right_color = texture2D(texture, right_pixel.xy);
  float right_intensity = right_color.r * 0.3 + right_color.g * 0.6 + right_color.b * 0.1;

  float total_intensity = (up_intensity + down_intensity + left_intensity + right_intensity) - 4.0*original_intensity;
  total_intensity *= 5;


  gl_FragColor = vec4(total_intensity,total_intensity,total_intensity, 1.0);
}

