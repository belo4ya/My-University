export const clear = (canvas) => {
    const ctx = canvas.getContext('2d');
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.restore();
}

export const drawPoint = (canvas, {x, y, r, color}) => {
    const ctx = canvas.getContext('2d');
    [x, y] = [x * canvas.width, y * canvas.height];
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2, true);
    ctx.fill();
}
