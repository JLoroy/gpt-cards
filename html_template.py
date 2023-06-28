css_template = """
<style>
    .container {
        margin: 20px;
        width: 300px;
        height: 400px;
        border-radius: 10px;
        overflow: hidden;
        position: relative;
        box-sizing: border-box;
    }

    .container.ether {
        color: #000000;
        background-color: #c280e8;
        background-image: url("app/static/Ether.png")
    }

    .container.arcane {
        color: #610059;
        background-color: #00d9ff;
        background-image: url("app/static/Arcane.png")
    }

    .container.chaos {
        color: #d80101;
        background-color: #000000;
        background-image: url("app/static/Chaos.png")
    }

    .container.nature {
        color: #e5ff7b;
        background-color: #208f52;
        background-image: url("app/static/Nature.png")
    }

    .container.spirit {
        color: #ffffff;
        background-color: #656565;
        background-image: url("app/static/Spirit.png")
    }

    .img-container {
        width: 100%;
        height: 65%;
        position: relative;
    }

    .img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .info-container {
        width: 100%;
        height: 35%;
        padding: 10px;
    }

    .info-container .info-row,
    .info-container .stats-row {
        display: flex;
        justify-content: space-between;
    }

    .info-container .info-row .name {
        font-weight: bold;
    }

    .info-container .info-row .hp {
        border-radius: 50%;
        background-color: red;
        padding: 5px;
    }

    .info-container .stats-row {
        margin: 1px 0;
    }

    .info-container .description {
        font-style: italic;
        text-align: center;
        font-size: x-small;
    }
</style>
"""