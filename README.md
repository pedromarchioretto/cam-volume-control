# Controle de Volume por Gestos Manuais

Este projeto permite controlar o volume do computador usando movimentos horizontais da sua mão, capturados por uma câmera. O ajuste de volume é ativado especificamente quando o dedo indicador e o polegar estão juntos.

---

## Funcionalidades

* **Ativação por Gesto Específico:** O controle de volume é ativado apenas quando o dedo indicador e o polegar estão em contato ou muito próximos.
* **Mapeamento de Posição para Volume:** A posição horizontal da sua mão na tela (da esquerda para a direita) é mapeada para o nível de volume do sistema.
* **Ajuste de Volume em Tempo Real:** O volume do sistema operacional é modificado dinamicamente conforme você move sua mão horizontalmente.

---

## Tecnologias Utilizadas

* **Python:** Linguagem de programação.
* **OpenCV:** Para captura e processamento de vídeo da câmera.
* **Mediapipe:** Para detecção e rastreamento dos pontos chave (landmarks) da mão.
* **Bibliotecas de Controle de Áudio:** Módulos específicos para interagir com o volume do sistema operacional.

---
