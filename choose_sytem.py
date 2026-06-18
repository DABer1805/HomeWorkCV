import hashlib

# Мне выпала debian:10.3, но я так понял, что 10-е версии сейчас не поддерживаются
# Так, что я поставил debian:11-slim
name = 'Бережной Дмитрий Анатольевич'

systems = [
    'debian:10.1',
    'debian:10.2',
    'debian:10.3',
    'debian:10.8',
    'ubuntu:20.04',
    'ubuntu:20.10',
    'ubuntu:18.04',
    'ubuntu:18.10',
    'fedora:33',
    'fedora:32',
    'fedora:31',
]

print(systems[int(hashlib.md5(name.encode('utf-8')).hexdigest(), 16) % len(systems)])