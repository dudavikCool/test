#version 330 core

layout (location=0) in vec3 vertexPos;
layout (location=1) in vec3 vertexNormal;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec3 fragPos;
out vec3 normal;

void main()
{      
    gl_Position = projection * view * model * vec4(vertexPos, 1.0f);

    fragPos = vec3(model * vec4(vertexPos, 1.0));
    normal = mat3(transpose(inverse(model))) * vertexNormal; 
}