#define PROCESSING_TEXTURE_SHADER
//Jiazheng Sun
uniform mat4 transform;
uniform mat4 texMatrix;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;

uniform sampler2D texture;

void main() {
  vertColor = color;
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);

  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  float original_R = diffuse_color.r * 0.3;
  float original_G = diffuse_color.g * 0.6;
  float original_B = diffuse_color.b * 0.1;
  float original_intensity = original_R + original_G + original_B;
  original_intensity *= 150;
  vec3 temp = normal * original_intensity;
  vec4 pos = position + vec4(temp,0);
  gl_Position = transform * pos;

}
