#include <stdio.h>

int main() {
    double x = 1.0;     // 初期位置
    double v = 0.0;     // 初期速度
    double k = 1.0;     // バネ定数
    double m = 1.0;     // 質量
    double dt = 0.01;   // 時間刻み
    double t = 0.0;
    
    FILE *fp = fopen("data.txt", "w");
    
    for (int i = 0; i < 1000; i++) {
        fprintf(fp, "%f %f\n", t, x);
        
        // オイラー法による更新
        double a = - (k / m) * x; // 加速度
        v += a * dt;
        x += v * dt;
        t += dt;
    }
    
    fclose(fp);
    printf("計算完了: data.txt を作成しました。\n");
    return 0;
}