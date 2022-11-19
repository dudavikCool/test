#version 330 core

in vec3 normal;  
in vec3 fragPos;  
out vec4 color;

uniform vec3 lightPosition; 

void main()
{ 
    vec3 normal = normalize(normal);
    vec3 lightDir = normalize(lightPosition - fragPos);
    float diff = max(dot(normal, lightDir), 0.0);
    vec3 diffuse = vec3(diff);

    color = vec4(diffuse, 1.0);
}