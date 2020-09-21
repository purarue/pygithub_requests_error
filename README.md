Debugging/Scripts for a issue made on PyGithub

Token scopes: ![](https://i.imgur.com/OMFrNnK.png)

- Create `token.json` (see `token.json.dist` for an example, put a token in that)
- run `./run`

Originally discovered <https://github.com/karlicoss/ghexport/issues/4>

This is example code to (possibly?) reproduce an error with PyGithub. From the discussion [here](https://github.com/karlicoss/ghexport/issues/4), @karlicoss was't able to reproduce it.

This is run on an `arch` machine, though I don't think that makes any difference.

This seems to be a `PyGithub`/`requests` error, since even just requesting something basic to github with the python `requests` fails (see `./requests_fails.py`, when the analogous `curl` command works fine.

See <https://github.com/karlicoss/ghexport/issues/4#issuecomment-693694338>; in which I use `pdb` to step into right before the request is made. If I make the request with the `requests` module, it fails. If I make it with `httpx`, it succeeds.

Similarly, I can subclass the `PyGithub` HTTPSRequestsConnectionClass to use `httpx` (another HTTP library), and then `PyGithub` works fine.

I'm unsure how I'd debug a failing `requests.get` any further, it doesn't feel like something that should fail.

Believe I've removed all instances of my token from this, but its deleted in any case.

For output, see `log.txt`

`curl

```
httpx==0.14.3
  - certifi [required: Any, installed: 2020.6.20]
  - chardet [required: ==3.*, installed: 3.0.4]
  - httpcore [required: ==0.10.*, installed: 0.10.2]
    - h11 [required: >=0.8,<0.10, installed: 0.9.0]
    - sniffio [required: ==1.*, installed: 1.1.0]
  - rfc3986 [required: >=1.3,<2, installed: 1.4.0]
  - sniffio [required: Any, installed: 1.1.0]
PyGithub==1.53
  - deprecated [required: Any, installed: 1.2.10]
    - wrapt [required: >=1.10,<2, installed: 1.12.1]
  - pyjwt [required: Any, installed: 1.7.1]
  - requests [required: >=2.14.0, installed: 2.24.0]
    - certifi [required: >=2017.4.17, installed: 2020.6.20]
    - chardet [required: >=3.0.2,<4, installed: 3.0.4]
    - idna [required: >=2.5,<3, installed: 2.10]
    - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.10]
```
