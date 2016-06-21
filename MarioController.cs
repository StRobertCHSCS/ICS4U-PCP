using UnityEngine;
using System.Collections;

public class MarioController : MonoBehaviour {

    public float moveSpeed;
    public float jumpHeight;

    public Transform groundCheck2;
    public float groundCheckRadius;
    public LayerMask whatIsGround;
    private bool grounded;

    private bool doubleJumped;

    private Animator anim;

    public Transform firePoint_right, firePoint_left;
    public GameObject fireBall;

    // Use this for initialization
    void Start () {
	
	}

    void FixedUpdate()
    {
        grounded = Physics2D.OverlapCircle(groundCheck2.position, groundCheckRadius, whatIsGround);
    }
    // Update is called once per frame
    void Update()
    {
        if (grounded)
            doubleJumped = false;

        if (Input.GetKeyDown(KeyCode.I) && grounded)
        {
            //GetComponent<Rigidbody2D>().velocity = new Vector2 (GetComponent<Rigidbody2D>().velocity.x, jumpHeight);
            Jump();
        }

        if (Input.GetKeyDown(KeyCode.I) && !doubleJumped && !grounded)
        {
            //GetComponent<Rigidbody2D>().velocity = new Vector2 (GetComponent<Rigidbody2D>().velocity.x, jumpHeight);
            Jump();
            doubleJumped = true;
        }

        if (Input.GetKey(KeyCode.L))
        {
            GetComponent<Rigidbody2D>().velocity = new Vector2(moveSpeed, GetComponent<Rigidbody2D>().velocity.y);
            //anim.SetFloat("Speed Right", Mathf.Abs(GetComponent<Rigidbody2D> ().velocity.x));
        }

        if (Input.GetKey(KeyCode.J))
        {
            GetComponent<Rigidbody2D>().velocity = new Vector2(-moveSpeed, GetComponent<Rigidbody2D>().velocity.y);
            //anim.SetFloat("Speed Left", Mathf.Abs(GetComponent<Rigidbody2D> ().velocity.x));
        }

        if (Input.GetKeyDown(KeyCode.M))
        {
            if (GetComponent<Rigidbody2D>().velocity.x > 0)
                Instantiate(fireBall, firePoint_right.position, firePoint_right.rotation);
            else if (GetComponent<Rigidbody2D>().velocity.x < 0)
                Instantiate(fireBall, firePoint_left.position, firePoint_left.rotation);
        }
    }

    public void Jump()
    {
        GetComponent<Rigidbody2D>().velocity = new Vector2(GetComponent<Rigidbody2D>().velocity.x, jumpHeight);
    }
}
