start：[[2024-11-05]] 19:47

[python - Import pyaudio doesn't work - Symbol not found: \_PaMacCore_SetupChannelMap on mac (Big Sur M1 Apple Silicon) - Stack Overflow](https://stackoverflow.com/questions/65709212/import-pyaudio-doesnt-work-symbol-not-found-pamaccore-setupchannelmap-on-ma)

```python
 brew install portaudio --HEAD
 pip install pyaudio --global-option="build_ext" --global-option="-I/opt/homebrew/include" --global-option="-L/opt/homebrew/lib"
```

=> OK

❯ pip freeze
PyAudio==0.2.14

import エラーは sounddevice を事前に import すれば良い

- [Fetching Title#t1b4](https://github.com/OpenInterpreter/01/issues/68)

```python
import sounddevice
import pyaudio
```
