/*
 * Теневой Кодер: Arduino датчик дыхания для биомодуляции
 * Защищённая версия с калибровкой и защитой от перегрузки
 */

// Пин для датчика давления (MPX5010)
#define PRESSURE_PIN A0
// Пин для ШИМ выхода (управление усилителем)
#define PWM_PIN 9
// Пин для LED индикации
#define LED_PIN 13

// Параметры калибровки
float min_pressure = 0.5;  // минимальное давление (В)
float max_pressure = 4.5;  // максимальное давление (В)
float min_pwm = 50;         // минимальный ШИМ (0-255)
float max_pwm = 200;        // максимальный ШИМ (0-255)

// Защита от перегрузки
float max_voltage = 4.8;    // максимальное напряжение датчика
bool protection_enabled = true;

// Калибровочные данные
struct CalibrationData {
  float baseline_pressure;
  float breath_amplitude;
  float breath_rate;
  bool calibrated;
};

CalibrationData calibration = {0, 0, 0, false};

// Буфер для анализа дыхания
float breath_buffer[100];
int buffer_index = 0;
bool buffer_full = false;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(PRESSURE_PIN, INPUT);
  pinMode(PWM_PIN, OUTPUT);
  
  Serial.println("🔥 Теневой Кодер: Arduino датчик дыхания");
  Serial.println("Калибровка...");
  
  // Калибровка в течение 10 секунд
  calibrate_sensor();
}

void loop() {
  if (!calibration.calibrated) {
    Serial.println("❌ Датчик не откалиброван!");
    delay(1000);
    return;
  }
  
  // Читаем давление
  float pressure_voltage = analogRead(PRESSURE_PIN) * (5.0 / 1023.0);
  
  // Защита от перегрузки
  if (protection_enabled && pressure_voltage > max_voltage) {
    Serial.println("⚠️ ПЕРЕГРУЗКА! Отключение защиты...");
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);
    return;
  }
  
  // Добавляем в буфер
  breath_buffer[buffer_index] = pressure_voltage;
  buffer_index = (buffer_index + 1) % 100;
  if (buffer_index == 0) buffer_full = true;
  
  // Анализируем дыхание
  float breath_envelope = analyze_breath_pattern();
  
  // Преобразуем в ШИМ
  int pwm_value = map_breath_to_pwm(breath_envelope);
  
  // Управляем усилителем
  analogWrite(PWM_PIN, pwm_value);
  
  // Отправляем данные в Serial (для Python)
  send_breath_data(pressure_voltage, breath_envelope, pwm_value);
  
  delay(50); // 20 Гц обновление
}

void calibrate_sensor() {
  Serial.println("Дыши спокойно 10 секунд...");
  
  float sum = 0;
  int samples = 0;
  
  for (int i = 0; i < 1000; i++) { // 10 секунд при 100 Гц
    float voltage = analogRead(PRESSURE_PIN) * (5.0 / 1023.0);
    sum += voltage;
    samples++;
    
    // Индикация калибровки
    if (i % 100 == 0) {
      digitalWrite(LED_PIN, HIGH);
      delay(50);
      digitalWrite(LED_PIN, LOW);
    }
    
    delay(10);
  }
  
  calibration.baseline_pressure = sum / samples;
  calibration.calibrated = true;
  
  Serial.print("✅ Калибровка завершена. Базовое давление: ");
  Serial.print(calibration.baseline_pressure);
  Serial.println(" В");
  
  // Мигаем LED для подтверждения
  for (int i = 0; i < 5; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    delay(200);
  }
}

float analyze_breath_pattern() {
  if (!buffer_full && buffer_index < 10) return 0;
  
  // Находим размах дыхания
  float min_val = 5.0;
  float max_val = 0.0;
  
  int samples = buffer_full ? 100 : buffer_index;
  for (int i = 0; i < samples; i++) {
    if (breath_buffer[i] < min_val) min_val = breath_buffer[i];
    if (breath_buffer[i] > max_val) max_val = breath_buffer[i];
  }
  
  float amplitude = max_val - min_val;
  calibration.breath_amplitude = amplitude;
  
  return amplitude;
}

int map_breath_to_pwm(float breath_amplitude) {
  // Нормализуем амплитуду дыхания
  float normalized = constrain(breath_amplitude, 0, 2.0); // макс 2В размах
  normalized = normalized / 2.0; // 0-1
  
  // Преобразуем в ШИМ с учётом калибровки
  int pwm = min_pwm + (normalized * (max_pwm - min_pwm));
  
  return constrain(pwm, min_pwm, max_pwm);
}

void send_breath_data(float pressure, float envelope, int pwm) {
  // Отправляем данные в формате JSON для Python
  Serial.print("{\"pressure\":");
  Serial.print(pressure, 3);
  Serial.print(",\"envelope\":");
  Serial.print(envelope, 3);
  Serial.print(",\"pwm\":");
  Serial.print(pwm);
  Serial.print(",\"calibrated\":");
  Serial.print(calibration.calibrated ? "true" : "false");
  Serial.println("}");
}

void emergency_stop() {
  // Аварийная остановка
  analogWrite(PWM_PIN, 0);
  digitalWrite(LED_PIN, HIGH);
  Serial.println("🚨 АВАРИЙНАЯ ОСТАНОВКА!");
}
