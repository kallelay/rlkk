%% Regularized Linear Kramers Kronig (FUNCTION)
% * input:
%   Z: Complex impedance vector
%    f: frequency vector
%    lambda: Regularization parameters
%    fx: DRT frequency vector
%    addR0: include series resistance
% * output:
%    Zf: Reconstructed Zf
% * Configuration:
function Zf = rLKK(Z, f, lambda, fx, addR0)


%% Configuration

% Regularization Parameter lambda (typical 1e-2 to 1e-8; atypical 1e-12 to
% 1e2)
% larger = less reliability on measured data (more noise + distortion)

if ~exist('lambda','var') || isempty('lambda')
    lambda =  1e-5;
    warning('Setting lambda to 1e-5')
end

% DRT Frequency vector, which should cover the measurement
if ~exist('fx','var') || isempty('fx')
    fx = logspace(-4,8,100).';
    warning('Setting fx to 10^-4 to 10^8, 100 points')
else
    fx = fx(:);
end

% include resistance, by using inf
if exist('addR0','var') && addR0==1
 fx = [fx;inf];
 warning('Adding R0');
end


%% Init
Z= Z(:);
Z_ww0  = @(R,w,w0) R./(1j.*w./w0 + 1);
w = 1;
f = f(:).';

%% Construct Matrix A
A = Z_ww0(w,f.',fx.');
A = [real(A);imag(A)];

aa = size(A);
if isscalar(lambda)
    A = [A;lambda.*eye(size(A))];   
else
    dA = zeros(size(A));
    dA(1:size(A,1)/2,1:size(A,1)/2) = diag(lambda);
    dA(size(A,1)/2+1:size(A,1),1:size(A,1)/2,1) = diag(lambda);
    A = [A;dA];   
end

%% Construct vector b
b = [real(Z);imag(Z);zeros(size(Z,1)*2,1)];
Z = Z(:).';

%% Calculate rLKK (use second or third in case of a heavily failure)
x = A\b;
% x = (A'*A)\A'*b;
% x = lsqr(A,b,1e-12);

%% Reconstruct Z
bb = A*x;
bb = bb(1:end/2);
bb = bb(1:end/2) + 1j.*bb(end/2+1:end);
% bb = bb + min(real(Zrq)); % + 1j.*min(imag(Zrq));
bb = bb; % + 1j.*min(imag(Zrq));
Zf = bb;
end