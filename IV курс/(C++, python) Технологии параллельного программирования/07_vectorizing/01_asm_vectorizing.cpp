#include <iostream>

typedef struct {

	float x, y, z, w;

} Vector4;

using namespace std;

void SSE_Add(Vector4 *res, Vector4 *a, Vector4 *b)

{

	__asm {

		mov eax, a;

		mov ebx, b;

		movups xmm0, [eax];

		movups xmm1, [ebx];

		addps xmm1, xmm0;

		mov eax, res;

		movups[eax], xmm1;

	}

}

int main()

{

	Vector4 a = { 1, 1, 1, 1 };

	Vector4 b = { 2, 3, 4, 5 };

	Vector4 res;

	SSE_Add(&res, &a, &b);

	cout << "x=" << res.x << " y=" << res.y << " z=" << res.z << " w=" << res.w << endl;

	return 0;

}