import numpy as np

# Parameter
N = 100

# Matrix size
dim = 2 * N - 1

# Prefactor
prefactor = (N**2) / (2 * np.pi**2)

# Construct the tridiagonal matrix
main_diag = 2 * np.ones(dim)
off_diag = -1 * np.ones(dim - 1)

M = prefactor * (
    np.diag(main_diag) +
    np.diag(off_diag, k=1) +
    np.diag(off_diag, k=-1)
)

# --- Construct f (diagonal matrix) ---
k = np.arange(-(N - 1), N)  # indices from -(N-1) to (N-1)
f_diag = np.sin(k * np.pi / N)

f = np.diag(f_diag)

# --- Full matrix ---
M_total = M + f

# Compute eigenvalues (matrix is symmetric)
eigenvalues = np.linalg.eigvalsh(M_total)

# Print eigenvalues
print("Eigenvalues for N = 100:")
print(eigenvalues)
